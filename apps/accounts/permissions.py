from rest_framework.permissions import BasePermission


class HasModelPermission(BasePermission):
    """
    Custom DRF permission that checks if request.user has the specific model
    permission specified by `required_permission` attribute on the view class.
    Example:
        required_permission = 'users.view_user'
    """
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False

        if request.user.is_superuser:
            return True

        permission = getattr(view, "required_permission", None)
        if not permission:
            return False

        return request.user.has_perm(permission)
