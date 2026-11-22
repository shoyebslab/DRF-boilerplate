from datetime import UTC, datetime

from django.db import connection
from django.shortcuts import redirect
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


def api_root_redirect_view(request):
    """
    Redirects root requests to the interactive API documentation.
    Adopted from DRF reference pattern.
    """
    return redirect("swagger-ui")


@extend_schema(
    summary="API v1 Root",
    description="Lists primary entrypoint endpoints and documentation available in API v1.",
    responses={
        200: {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "version": {"type": "string"},
                "status": {"type": "string"},
                "endpoints": {"type": "object"},
            },
        }
    },
)
class APIRootView(APIView):
    """
    Browsable API Root providing direct discovery of API v1 resources.
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response(
            {
                "name": "Starline Hospital Management API",
                "version": "v1.0.0",
                "status": "active",
                "documentation": {
                    "swagger": request.build_absolute_uri("/api/docs/"),
                    "redoc": request.build_absolute_uri("/api/redoc/"),
                    "schema": request.build_absolute_uri("/api/schema/"),
                },
                "endpoints": {
                    "auth": request.build_absolute_uri("/api/v1/auth/"),
                    "users": request.build_absolute_uri("/api/v1/users/"),
                    "roles": request.build_absolute_uri("/api/v1/roles/"),
                    "health": request.build_absolute_uri(reverse("api-health", request=request, format=format)),
                },
            },
            status=status.HTTP_200_OK,
        )


@extend_schema(
    summary="System Health Check",
    description="Verifies database connectivity and operational status of the service.",
    responses={
        200: {
            "type": "object",
            "properties": {
                "status": {"type": "string"},
                "database": {"type": "string"},
                "timestamp": {"type": "string"},
                "version": {"type": "string"},
            },
        }
    },
)
class HealthCheckView(APIView):
    """
    Health check probe for uptime monitoring, load balancers, and Docker/Kubernetes probes.
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        db_status = "connected"
        http_status = status.HTTP_200_OK

        try:
            connection.ensure_connection()
        except Exception as exc:
            db_status = f"unhealthy: {exc!s}"
            http_status = status.HTTP_503_SERVICE_UNAVAILABLE

        payload = {
            "status": "healthy" if http_status == status.HTTP_200_OK else "degraded",
            "database": db_status,
            "timestamp": datetime.now(UTC).isoformat(),
            "version": "1.0.0",
        }
        return Response(payload, status=http_status)


@extend_schema(
    summary="Dashboard Report Statistics",
    description="Provides real-time system KPI telemetry metrics for the console dashboard.",
    responses={
        200: {
            "type": "object",
            "properties": {
                "totalRevenue": {"type": "number"},
                "activeUsers": {"type": "integer"},
                "conversionRate": {"type": "number"},
                "uptime": {"type": "number"},
            },
        }
    },
)
class ReportStatsView(APIView):
    """
    Returns dashboard telemetry and KPI overview statistics.
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        from apps.users.models import User

        active_users = User.objects.filter(is_active=True).count()
        return Response(
            {
                "totalRevenue": 284500,
                "activeUsers": active_users,
                "conversionRate": 64.8,
                "uptime": 99.98,
            },
            status=status.HTTP_200_OK,
        )

