from django.contrib.auth.models import Group, Permission
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.roles.permissions import IsRoleAdmin
from apps.roles.serializers.role import (
    AssignRoleSerializer,
    PermissionSerializer,
    RoleSerializer,
)
from apps.roles.services.role_service import assign_role
from apps.users.models import User


@extend_schema_view(
    get=extend_schema(
        summary="List all roles",
        description="Retrieve all user groups / roles and their assigned permissions.",
        responses={200: RoleSerializer(many=True)},
    ),
    post=extend_schema(
        summary="Create a new role",
        description="Create a new role group and optionally attach permissions.",
        request=RoleSerializer,
        responses={201: RoleSerializer},
    ),
)
class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.prefetch_related("permissions").all().order_by("id")
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated, IsRoleAdmin]


@extend_schema_view(
    get=extend_schema(summary="Retrieve role details", responses={200: RoleSerializer}),
    put=extend_schema(summary="Update role", request=RoleSerializer, responses={200: RoleSerializer}),
    patch=extend_schema(summary="Partial update role", request=RoleSerializer, responses={200: RoleSerializer}),
    delete=extend_schema(summary="Delete role", responses={204: None}),
)
class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.prefetch_related("permissions").all().order_by("id")
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated, IsRoleAdmin]


@extend_schema(
    summary="Assign role to user",
    description="Assigns a specified role to a user by ID.",
    request=AssignRoleSerializer,
    responses={200: {"type": "object", "properties": {"message": {"type": "string"}}}},
)
class AssignRoleView(APIView):
    permission_classes = [IsAuthenticated, IsRoleAdmin]

    def post(self, request, *args, **kwargs):
        serializer = AssignRoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(id=serializer.validated_data["user_id"])
        role_name = serializer.validated_data["role_name"]

        assign_role(user, role_name)

        return Response(
            {"message": f"Role '{role_name}' successfully assigned to user '{user.username}'."},
            status=status.HTTP_200_OK,
        )


@extend_schema(
    summary="List available permissions",
    description="List all system model permissions available to assign to roles.",
    responses={200: PermissionSerializer(many=True)},
)
class PermissionListView(generics.ListAPIView):
    queryset = Permission.objects.select_related("content_type").all().order_by("content_type__app_label", "codename")
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsRoleAdmin]
