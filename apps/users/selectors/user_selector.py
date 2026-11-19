
from django.db.models import QuerySet

from apps.users.models import User


def get_all_users() -> QuerySet[User]:
    """
    Returns all users with prefetched groups, ordered by created_at descending.
    """
    return User.objects.prefetch_related("groups").all().order_by("-created_at")


def get_user_by_id(user_id: int) -> User | None:
    """
    Returns a single user by primary key, or None if not found.
    """
    return User.objects.prefetch_related("groups", "user_permissions").filter(id=user_id).first()


def get_user_by_email(email: str) -> User | None:
    """
    Returns a single user by email address, or None if not found.
    """
    return User.objects.filter(email__iexact=email).first()


def get_users_by_role(role: str) -> QuerySet[User]:
    """
    Returns users filtered by role name.
    """
    return User.objects.filter(role=role).order_by("-created_at")
