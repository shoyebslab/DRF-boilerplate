from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.accounts.serializers.login import CustomTokenObtainPairSerializer
from apps.accounts.serializers.register import RegisterSerializer
from apps.accounts.serializers.user import ChangePasswordSerializer, UserProfileSerializer
from apps.accounts.services.auth_service import change_user_password, log_activity
from common.utils.helpers import get_client_ip


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Takes a set of user credentials (username/email & password) and returns
    access and refresh JSON web token pair along with user info.
    """
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            # Optionally log user login
            pass
        return response


@extend_schema(
    summary="Register a new account",
    description="Creates a new account and returns the created user record.",
    request=RegisterSerializer,
    responses={201: UserProfileSerializer},
)
class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        log_activity(
            user=user,
            action="Account Registered",
            ip_address=get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", "")
        )
        output_serializer = UserProfileSerializer(user)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(
    summary="Change user password",
    description="Updates the authenticated user's password.",
    request=ChangePasswordSerializer,
    responses={200: {"type": "object", "properties": {"message": {"type": "string"}}}},
)
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        change_user_password(request.user, serializer.validated_data["new_password"])
        log_activity(
            user=request.user,
            action="Password Changed",
            ip_address=get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", "")
        )
        return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)
