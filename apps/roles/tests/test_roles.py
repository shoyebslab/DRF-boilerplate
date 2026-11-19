from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.roles.services.role_service import assign_role, create_role

User = get_user_model()


class RolesAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser(
            username="role_superadmin",
            email="role_admin@starline.com",
            password="AdminPassword123!",
            role="Admin"
        )
        self.client.force_authenticate(user=self.admin)

    def test_create_and_list_roles(self):
        create_role(name="TestRole")
        response = self.client.get("/api/v1/roles/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        role_names = [item["name"] for item in response.data["results"]]
        self.assertIn("TestRole", role_names)

    def test_assign_role_service(self):
        user = User.objects.create_user(
            username="normaluser",
            email="normal@starline.com",
            password="NormalPassword123!"
        )
        role = create_role(name="Doctor")
        assign_role(user, role)
        user.refresh_from_db()
        self.assertEqual(user.role, "Doctor")
        self.assertTrue(user.groups.filter(name="Doctor").exists())
