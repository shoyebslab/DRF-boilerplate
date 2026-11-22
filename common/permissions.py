from rest_framework.permissions import SAFE_METHODS, BasePermission, DjangoModelPermissions


class IsSuperAdminUser(BasePermission):
    """
    Allows access only to superusers.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class HasAnyRole(BasePermission):
    """
    Checks if authenticated user belongs to any of the specified roles (groups).
    Can be used by setting `allowed_roles = ['Admin', 'Manager']` on view
    or initializing HasAnyRole(['Admin', 'Doctor']).
    """
    def __init__(self, allowed_roles=None):
        self.allowed_roles = allowed_roles or []

    def __call__(self):
        return self

    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False

        if request.user.is_superuser:
            return True

        roles = getattr(view, "allowed_roles", self.allowed_roles)
        if not roles:
            return True

        # Check if user has explicit role field or belongs to the group
        user_role = getattr(request.user, "role", None)
        if user_role:
            normalized_roles = [str(r).upper() for r in roles]
            if str(user_role).upper() in normalized_roles:
                return True
            if str(user_role).upper() in ["SUPER_ADMIN", "ADMIN"] and any(r in ["ADMIN", "SUPER_ADMIN"] for r in normalized_roles):
                return True

        return request.user.groups.filter(name__in=roles).exists()


class HasModelPermission(BasePermission):
    """
    Enforces Django model permission checks (e.g. 'users.view_user').
    View must specify `required_permission = 'app_label.action_model'`.
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


class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # Support common ownership attributes
        owner = getattr(obj, "user", getattr(obj, "author", getattr(obj, "owner", None)))
        if owner is not None:
            return owner == request.user

        if obj == request.user:
            return True

        return False


class IsAdminOrReadOnly(BasePermission):
    """
    Allows read-only access for safe methods (GET, HEAD, OPTIONS) to all users,
    while restricting write actions (POST, PUT, PATCH, DELETE) to staff/admin users.
    Adopted from DRF reference standard.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class FullDjangoModelPermission(DjangoModelPermissions):
    """
    Extends DjangoModelPermissions to also require view permissions on GET requests.
    Adopted from DRF reference standard.
    """
    def __init__(self):
        super().__init__()
        self.perms_map["GET"] = ["%(app_label)s.view_%(model_name)s"]

