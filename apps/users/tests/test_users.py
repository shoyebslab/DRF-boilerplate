from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_group = Group.objects.create(name="Admin")
        self.admin_user = User.objects.create_superuser(
            username="adminuser",
            email="admin@starline.com",
            password="AdminPassword123!",
            role="Admin"
        )
        self.admin_user.groups.add(self.admin_group)

        self.patient_user = User.objects.create_user(
            username="patientuser",
            email="patient@starline.com",
            password="PatientPassword123!",
            role="Patient"
        )

    def test_list_users_as_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get("/api/v1/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data["results"]) >= 2)

    def test_list_users_forbidden_for_patient(self):
        self.client.force_authenticate(user=self.patient_user)
        response = self.client.get("/api/v1/users/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_user_service_and_api(self):
        self.client.force_authenticate(user=self.admin_user)
        payload = {
            "username": "doctor_strange",
            "email": "doctor@starline.com",
            "password": "SecureDoctor123!",
            "phone": "+1234567890",
            "role": "Doctor",
            "first_name": "Stephen",
            "last_name": "Strange",
        }
        response = self.client.post("/api/v1/users/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["email"], "doctor@starline.com")
        self.assertTrue(User.objects.filter(username="doctor_strange").exists())
