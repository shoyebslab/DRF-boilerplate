from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from apps.api.views import api_root_redirect_view

urlpatterns = [
    # Root entrypoint redirect to API documentation (adopted from DRF reference)
    path("", api_root_redirect_view, name="root-redirect"),

    # Admin Dashboard
    path("admin/", admin.site.urls),

    # Browsable API authentication login/logout (adopted from DRF reference)
    path("api-auth/", include("rest_framework.urls")),

    # Centralized Versioned API Endpoints (v1)
    path("api/v1/", include("apps.api.urls")),

    # OpenAPI Schema & Interactive Documentation (supporting /swagger/ like in DRF & /api/docs/)
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui-alias"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc-alias"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

# Development Debug Toolbar & Static Media Serving
if settings.DEBUG:
    try:
        from debug_toolbar.toolbar import debug_toolbar_urls

        urlpatterns += debug_toolbar_urls()
    except (ImportError, Exception):
        pass

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
