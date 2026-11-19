from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.views import APIView

from apps.accounts.permissions import HasModelPermission

User = get_user_model()


class DummyProtectedView(APIView):
    permission_classes = [HasModelPermission]
    required_permission = "users.view_user"

    def get(self, request):
        return Response({"message": "Authorized"})


class PermissionsTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user_with_perm = User.objects.create_user(
            username="permitted_user",
            email="perm@starline.com",
            password="PermPass123!"
        )
        self.user_without_perm = User.objects.create_user(
            username="unpermitted_user",
            email="noperm@starline.com",
            password="NoPermPass123!"
        )
        perm = Permission.objects.get(codename="view_user")
        self.user_with_perm.user_permissions.add(perm)

    def test_user_with_model_permission(self):
        request = self.factory.get("/")
        force_authenticate(request, user=self.user_with_perm)
        view = DummyProtectedView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_user_without_model_permission(self):
        request = self.factory.get("/")
        force_authenticate(request, user=self.user_without_perm)
        view = DummyProtectedView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 403)
