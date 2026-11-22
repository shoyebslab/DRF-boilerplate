from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
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

User = get_user_model()


@extend_schema(
    summary="Obtain JWT token pair",
    description="Authenticate with username/email and password to obtain JWT access/refresh tokens and complete user profile details.",
    request=CustomTokenObtainPairSerializer,
)
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Takes a set of user credentials (username/email & password) and returns
    access and refresh JSON web token pair along with user info.
    """
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            try:
                username_or_email = request.data.get("username") or request.data.get("email")
                if username_or_email:
                    user = (
                        User.objects.filter(email__iexact=username_or_email).first()
                        or User.objects.filter(username__iexact=username_or_email).first()
                    )
                    if user:
                        log_activity(
                            user=user,
                            action="User Logged In",
                            ip_address=get_client_ip(request),
                            user_agent=request.META.get("HTTP_USER_AGENT", "")
                        )
            except Exception:
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


@extend_schema(
    summary="Request password reset",
    description="Initiates password reset by email. Generates reset token if the account exists.",
    responses={200: {"type": "object", "properties": {"detail": {"type": "string"}}}},
)
class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = (request.data.get("email") or "").strip()
        if email:
            user = User.objects.filter(email__iexact=email).first()
            if user:
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                log_activity(
                    user=user,
                    action=f"Password Reset Requested (token: {uid}_{token})",
                    ip_address=get_client_ip(request),
                    user_agent=request.META.get("HTTP_USER_AGENT", "")
                )
        return Response(
            {"detail": "If an account exists with this email, password reset instructions have been sent."},
            status=status.HTTP_200_OK,
        )


@extend_schema(
    summary="Confirm password reset",
    description="Resets the user's password using the token received in reset link.",
    responses={200: {"type": "object", "properties": {"detail": {"type": "string"}}}},
)
class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token_str = (request.data.get("token") or "").strip()
        new_password = (request.data.get("password") or "").strip()

        if not token_str or not new_password:
            return Response(
                {"detail": "Token and new password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            uidb64, token = token_str.split("_", 1)
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception:
            return Response(
                {"detail": "Invalid or expired reset token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not default_token_generator.check_token(user, token):
            return Response(
                {"detail": "Invalid or expired reset token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(new_password)
        user.save()
        log_activity(
            user=user,
            action="Password Reset Completed",
            ip_address=get_client_ip(request),
            user_agent=request.META.get("HTTP_USER_AGENT", "")
        )
        return Response(
            {"detail": "Password has been reset successfully."},
            status=status.HTTP_200_OK,
        )
