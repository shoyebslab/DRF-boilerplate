from django.contrib.auth import get_user_model
from rest_framework import serializers

from common.constants import ROLE_FRONTEND_PERMISSIONS, normalize_role
from common.validators import validate_password_strength

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    permissions = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()
    date_joined = serializers.DateTimeField(read_only=True)
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "role",
            "permissions",
            "avatar",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "date_joined",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "username",
            "role",
            "permissions",
            "avatar",
            "is_staff",
            "is_superuser",
            "date_joined",
            "created_at",
            "updated_at",
        ]

    def get_role(self, obj) -> str:
        return normalize_role(obj)

    def get_permissions(self, obj) -> list:
        role = self.get_role(obj)
        return ROLE_FRONTEND_PERMISSIONS.get(role, [])

    def get_avatar(self, obj):
        return None


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password_strength]
    )

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("Current password does not match.")
        return value
