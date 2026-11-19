from django.contrib.auth import get_user_model
from django.test import TestCase
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
            role="Patient"
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

    def test_jwt_login_with_email(self):
        payload = {
            "username": "testauth@starline.com",
            "password": self.user_password,
        }
        response = self.client.post("/api/v1/auth/login/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

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
