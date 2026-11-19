
from django.contrib.auth.models import Group, Permission
from django.db import transaction

from apps.users.models import User


@transaction.atomic
def create_role(name: str, permissions: list[int | Permission] | None = None) -> Group:
    """
    Creates or retrieves a role (Group) and assigns permissions.
    """
    role, _ = Group.objects.get_or_create(name=name)

    if permissions is not None:
        role.permissions.set(permissions)

    return role


@transaction.atomic
def assign_role(user: User, role: Group | str) -> None:
    """
    Assigns a role (Group) to a user and synchronizes the role attribute.
    """
    if isinstance(role, str):
        role_obj, _ = Group.objects.get_or_create(name=role)
    else:
        role_obj = role

    user.groups.add(role_obj)
    user.role = role_obj.name
    user.save(update_fields=["role"])


@transaction.atomic
def remove_role(user: User, role: Group | str) -> None:
    """
    Removes a role (Group) from a user.
    """
    if isinstance(role, str):
        role_obj = Group.objects.filter(name=role).first()
        if not role_obj:
            return
    else:
        role_obj = role

    user.groups.remove(role_obj)
    if user.role == role_obj.name:
        remaining_role = user.groups.first()
        user.role = remaining_role.name if remaining_role else "Viewer"
        user.save(update_fields=["role"])


def get_user_roles(user: User):
    """
    Retrieves all roles assigned to a user.
    """
    return user.groups.all()
