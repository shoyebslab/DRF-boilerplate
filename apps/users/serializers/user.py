from rest_framework import serializers

from apps.users.models import User
from common.validators import validate_password_strength, validate_phone_number


class UserSerializer(serializers.ModelSerializer):
    """
    Standard User representation serializer.
    """
    groups_list = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
        source="groups"
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "role",
            "first_name",
            "last_name",
            "is_active",
            "groups_list",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class UserListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for listing users.
    """
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "role",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Comprehensive serializer for retrieving single user details.
    """
    groups_list = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
        source="groups"
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "role",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "groups_list",
            "created_at",
            "updated_at",
            "last_login",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "last_login"]


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new user with password validation.
    """
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password_strength],
        style={"input_type": "password"}
    )
    phone = serializers.CharField(
        required=False,
        allow_blank=True,
        validators=[validate_phone_number]
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "phone",
            "role",
            "first_name",
            "last_name",
        ]

    def create(self, validated_data):
        from apps.users.services.user_service import create_user
        return create_user(validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating an existing user's profile info.
    """
    phone = serializers.CharField(
        required=False,
        allow_blank=True,
        validators=[validate_phone_number]
    )

    class Meta:
        model = User
        fields = [
            "email",
            "phone",
            "role",
            "first_name",
            "last_name",
            "is_active",
        ]
