from django.contrib.auth.models import Group
from django.db import transaction

from apps.users.models import User


@transaction.atomic
def create_user(validated_data: dict) -> User:
    """
    Service to create a new user, hashes password, assigns default role group.
    """
    password = validated_data.pop("password")
    role_name = validated_data.get("role")

    user = User.objects.create_user(
        password=password,
        **validated_data
    )

    if role_name:
        group, _ = Group.objects.get_or_create(name=role_name)
        user.groups.add(group)

    return user


@transaction.atomic
def update_user(user: User, validated_data: dict) -> User:
    """
    Service to update an existing user's details and sync role group.
    """
    role_name = validated_data.get("role")
    if role_name and role_name != user.role:
        # Sync group membership
        old_group = Group.objects.filter(name=user.role).first()
        if old_group:
            user.groups.remove(old_group)
        new_group, _ = Group.objects.get_or_create(name=role_name)
        user.groups.add(new_group)

    for attr, value in validated_data.items():
        setattr(user, attr, value)

    user.save()
    return user


@transaction.atomic
def delete_user(user: User) -> None:
    """
    Service to delete or deactivate a user.
    """
    user.delete()
