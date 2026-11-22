from django.urls import path
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenRefreshView,
    TokenVerifyView,
)

from apps.accounts.views.auth import (
    ChangePasswordView,
    CustomTokenObtainPairView,
    PasswordResetConfirmView,
    PasswordResetRequestView,
    RegisterView,
)
from apps.accounts.views.profile import UserProfileView

urlpatterns = [
    # JWT Authentication Endpoints (SimpleJWT standard & aliases)
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("verify/", TokenVerifyView.as_view(), name="verify"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),

    # User Profile / Current User Endpoints (frontend calls /auth/users/me/)
    path("users/me/", UserProfileView.as_view(), name="user_me"),
    path("profile/", UserProfileView.as_view(), name="profile"),

    # Password Management & Registration
    path("password/reset/", PasswordResetRequestView.as_view(), name="password_reset_request"),
    path("password/reset/confirm/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("register/", RegisterView.as_view(), name="register"),
]
