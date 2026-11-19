from django.urls import path

from apps.roles.views.role import (
    AssignRoleView,
    PermissionListView,
    RoleDetailView,
    RoleListCreateView,
)

urlpatterns = [
    path("", RoleListCreateView.as_view(), name="role-list"),
    path("<int:pk>/", RoleDetailView.as_view(), name="role-detail"),
    path("assign/", AssignRoleView.as_view(), name="role-assign"),
    path("permissions/", PermissionListView.as_view(), name="permission-list"),
]
