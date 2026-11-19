from django.contrib.auth.models import Group, Permission

# Roles in this architecture leverage Django's built-in Group and Permission models
# to provide robust, battle-tested RBAC.
Role = Group

__all__ = ["Role", "Permission"]
