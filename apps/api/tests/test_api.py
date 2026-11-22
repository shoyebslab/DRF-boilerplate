from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from rest_framework.views import APIView

from apps.api.permissions import FullDjangoModelPermission, IsAdminOrReadOnly

User = get_user_model()


class DummyProtectedView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        return Response({"status": "read"})

    def post(self, request):
        return Response({"status": "created"}, status=status.HTTP_201_CREATED)


class DummyModelPermissionView(APIView):
    permission_classes = [FullDjangoModelPermission]

    def get(self, request):
        return Response({"status": "viewed"})


class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.regular_user = User.objects.create_user(
            username="testuser",
            email="testuser@starline.com",
            password="TestPassword123!",
            is_staff=False,
        )
        self.staff_user = User.objects.create_user(
            username="staffuser",
            email="staffuser@starline.com",
            password="StaffPassword123!",
            is_staff=True,
        )

    def test_root_redirect_to_swagger(self):
        """Root URL / should redirect to Swagger docs."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertIn("/api/docs/", response.url)

    def test_swagger_and_redoc_endpoints(self):
        """Verify Swagger UI and ReDoc load successfully at all configured endpoints."""
        for endpoint in ["/swagger/", "/api/docs/", "/redoc/", "/api/redoc/"]:
            with self.subTest(endpoint=endpoint):
                res = self.client.get(endpoint)
                self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_v1_root(self):
        """GET /api/v1/ should return API root metadata with discovery links."""
        response = self.client.get("/api/v1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("status"), "active")
        self.assertIn("endpoints", response.data)
        self.assertIn("documentation", response.data)

    def test_health_check_endpoint(self):
        """GET /api/v1/health/ should report system and database health."""
        response = self.client.get("/api/v1/health/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("status"), "healthy")
        self.assertEqual(response.data.get("database"), "connected")

    def test_is_admin_or_read_only_safe_methods(self):
        """Unauthenticated or regular user can perform GET (safe method)."""
        request = self.factory.get("/")
        view = DummyProtectedView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_is_admin_or_read_only_write_forbidden_for_regular_user(self):
        """Regular non-staff user cannot perform POST."""
        request = self.factory.post("/")
        force_authenticate(request, user=self.regular_user)
        view = DummyProtectedView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_is_admin_or_read_only_write_allowed_for_staff(self):
        """Staff user can perform POST."""
        request = self.factory.post("/")
        force_authenticate(request, user=self.staff_user)
        view = DummyProtectedView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
