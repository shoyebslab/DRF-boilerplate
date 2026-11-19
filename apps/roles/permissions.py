from rest_framework.permissions import BasePermission

from common.constants import RoleConstants


class IsRoleAdmin(BasePermission):
    """
    Grants access only to Superusers or Users with Admin role.
    """
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False

        if request.user.is_superuser:
            return True

        if getattr(request.user, "role", None) == RoleConstants.ADMIN:
            return True

        return request.user.groups.filter(name=RoleConstants.ADMIN).exists()
