from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication & Profile APIs
    path("api/v1/auth/", include("apps.accounts.urls")),

    # User Management APIs
    path("api/v1/users/", include("apps.users.urls")),

    # Role & Permission APIs (RBAC)
    path("api/v1/roles/", include("apps.roles.urls")),

    # OpenAPI Schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    # Swagger UI & ReDoc
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
