from django.urls import include, path

from apps.api.views import APIRootView, HealthCheckView

urlpatterns = [
    # API v1 Discovery Root & Health
    path("", APIRootView.as_view(), name="api-v1-root"),
    path("health/", HealthCheckView.as_view(), name="api-health"),

    # Domain Endpoints
    path("auth/", include("apps.accounts.urls")),
    path("users/", include("apps.users.urls")),
    path("roles/", include("apps.roles.urls")),
]
