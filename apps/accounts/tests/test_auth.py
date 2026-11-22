from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.test import TestCase
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


class AuthenticationAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_password = "SecretPassword123!"
        self.user = User.objects.create_user(
            username="testauthuser",
            email="testauth@starline.com",
            password=self.user_password,
            first_name="Test",
            last_name="User",
            role="Patient"
        )
        self.admin = User.objects.create_superuser(
            username="testadmin",
            email="admin@starline.com",
            password="AdminPassword123!",
            first_name="Admin",
            last_name="Super",
        )

    def test_jwt_login_with_username(self):
        payload = {
            "username": "testauthuser",
            "password": self.user_password,
        }
        response = self.client.post("/api/v1/auth/login/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("user", response.data)
        self.assertEqual(response.data["user"]["email"], "testauth@starline.com")

    def test_jwt_login_with_email_via_token_endpoint(self):
        payload = {
            "email": "testauth@starline.com",
            "password": self.user_password,
        }
        response = self.client.post("/api/v1/auth/token/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("user", response.data)
        self.assertEqual(response.data["user"]["username"], "testauthuser")

    def test_admin_login_returns_super_admin_role_and_permissions(self):
        payload = {
            "username": "testadmin",
            "email": "admin@starline.com",
            "password": "AdminPassword123!",
        }
        response = self.client.post("/api/v1/auth/token/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user_data = response.data["user"]
        self.assertEqual(user_data["role"], "SUPER_ADMIN")
        self.assertTrue(user_data["is_superuser"])
        self.assertIn("users:view", user_data["permissions"])
        self.assertIn("roles:view", user_data["permissions"])

    def test_users_me_endpoint_returns_current_profile(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get("/api/v1/auth/users/me/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testadmin")
        self.assertEqual(response.data["role"], "SUPER_ADMIN")
        self.assertIn("users:view", response.data["permissions"])

    def test_token_refresh_endpoint(self):
        login_res = self.client.post("/api/v1/auth/token/", {
            "username": "testauthuser",
            "password": self.user_password,
        })
        refresh_token = login_res.data["refresh"]
        response = self.client.post("/api/v1/auth/token/refresh/", {"refresh": refresh_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_password_reset_flow(self):
        # 1. Request reset
        req_res = self.client.post("/api/v1/auth/password/reset/", {"email": "testauth@starline.com"})
        self.assertEqual(req_res.status_code, status.HTTP_200_OK)

        # 2. Confirm reset
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        reset_token = f"{uid}_{token}"

        confirm_res = self.client.post("/api/v1/auth/password/reset/confirm/", {
            "token": reset_token,
            "password": "BrandNewPassword123!",
        })
        self.assertEqual(confirm_res.status_code, status.HTTP_200_OK)

        # 3. Verify new password works
        login_res = self.client.post("/api/v1/auth/token/", {
            "email": "testauth@starline.com",
            "password": "BrandNewPassword123!",
        })
        self.assertEqual(login_res.status_code, status.HTTP_200_OK)

    def test_register_new_user(self):
        payload = {
            "username": "newuser",
            "email": "newuser@starline.com",
            "password": "NewUserPass123!",
            "password_confirm": "NewUserPass123!",
            "phone": "+19876543210",
        }
        response = self.client.post("/api/v1/auth/register/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_user_profile_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/v1/auth/profile/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testauthuser")
