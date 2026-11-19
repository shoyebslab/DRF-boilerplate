from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from apps.users.filters import UserFilter
from apps.users.models import User
from apps.users.selectors.user_selector import get_all_users
from apps.users.serializers.user import (
    UserCreateSerializer,
    UserDetailSerializer,
    UserListSerializer,
    UserUpdateSerializer,
)
from apps.users.services.user_service import delete_user, update_user
from common.constants import RoleConstants
from common.permissions import HasAnyRole


@extend_schema_view(
    get=extend_schema(
        summary="List all users",
        description="Retrieve a paginated list of users. Filter by username, email, role, etc.",
        responses={200: UserListSerializer(many=True)},
    ),
    post=extend_schema(
        summary="Create a new user",
        description="Creates a new user with hashed password and role assignment.",
        request=UserCreateSerializer,
        responses={201: UserDetailSerializer},
    ),
)
class UserListCreateView(ListCreateAPIView):
    """
    List and create users.
    Restricted to Admin and Manager roles.
    """
    permission_classes = [IsAuthenticated, HasAnyRole([RoleConstants.ADMIN, RoleConstants.MANAGER])]
    filterset_class = UserFilter
    search_fields = ["username", "email", "phone", "first_name", "last_name"]
    ordering_fields = ["created_at", "username", "email"]

    def get_queryset(self):
        return get_all_users()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserCreateSerializer
        return UserListSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Retrieve user details",
        description="Get detailed profile of a specific user by ID.",
        responses={200: UserDetailSerializer},
    ),
    put=extend_schema(
        summary="Update user details",
        description="Update all editable fields of a user.",
        request=UserUpdateSerializer,
        responses={200: UserDetailSerializer},
    ),
    patch=extend_schema(
        summary="Partially update user details",
        description="Partially update editable fields of a user.",
        request=UserUpdateSerializer,
        responses={200: UserDetailSerializer},
    ),
    delete=extend_schema(
        summary="Delete a user",
        description="Permanently remove a user record.",
        responses={204: None},
    ),
)
class UserDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a specific user.
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, HasAnyRole([RoleConstants.ADMIN, RoleConstants.MANAGER])]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return UserUpdateSerializer
        return UserDetailSerializer

    def perform_update(self, serializer):
        update_user(self.get_object(), serializer.validated_data)

    def perform_destroy(self, instance):
        delete_user(instance)
