from django.urls import path
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenRefreshView,
)

from apps.accounts.views.auth import (
    ChangePasswordView,
    CustomTokenObtainPairView,
    RegisterView,
)
from apps.accounts.views.profile import UserProfileView

urlpatterns = [
    # JWT Authentication Endpoints
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),

    # Registration & Account Management
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
]
