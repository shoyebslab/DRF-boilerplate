from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import transaction

from apps.accounts.models import UserActivityLog
from common.constants import RoleConstants

User = get_user_model()


@transaction.atomic
def register_user(validated_data: dict) -> User:
    """
    Registers a new user, defaults to 'Patient' role and adds them to Patient group.
    """
    password = validated_data.pop("password")
    role_name = validated_data.get("role", RoleConstants.PATIENT)
    validated_data["role"] = role_name

    user = User.objects.create_user(
        password=password,
        **validated_data
    )

    # Automatically add to default group
    group, _ = Group.objects.get_or_create(name=role_name)
    user.groups.add(group)

    return user


@transaction.atomic
def change_user_password(user: User, new_password: str) -> None:
    """
    Updates the password for a user.
    """
    user.set_password(new_password)
    user.save(update_fields=["password"])


def log_activity(user, action: str, ip_address: str = None, user_agent: str = ""):
    """
    Records an activity audit log.
    """
    UserActivityLog.objects.create(
        user=user,
        action=action,
        ip_address=ip_address,
        user_agent=user_agent
    )
