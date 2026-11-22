from django.urls import include, path

from apps.api.views import APIRootView, HealthCheckView, ReportStatsView
from apps.roles.views.role import PermissionListView

urlpatterns = [
    # API v1 Discovery Root & Health
    path("", APIRootView.as_view(), name="api-v1-root"),
    path("health/", HealthCheckView.as_view(), name="api-health"),

    # Domain Endpoints
    path("auth/", include("apps.accounts.urls")),
    path("users/", include("apps.users.urls")),
    path("roles/", include("apps.roles.urls")),
    path("settings/", include("apps.settings.urls")),
    path("permissions/", PermissionListView.as_view(), name="api-permissions"),
    path("reports/stats/", ReportStatsView.as_view(), name="api-reports-stats"),
]
