from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from common.constants import ROLE_FRONTEND_PERMISSIONS, normalize_role

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom JWT serializer that allows authentication using either
    username or email, and enriches token payload with user profile details.
    """
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.CharField(required=False, allow_blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field].required = False
        self.fields[self.username_field].allow_blank = True
        self.fields["email"] = serializers.CharField(
            required=False, allow_blank=True, write_only=True
        )

    def validate(self, attrs):
        username = (attrs.get("username") or "").strip()
        email = (attrs.get("email") or "").strip()
        identifier = username or email or (attrs.get(self.username_field) or "").strip()

        if not identifier:
            raise serializers.ValidationError({"email": "Email or username is required."})

        # Support email or username based login (case-insensitive)
        user = (
            User.objects.filter(email__iexact=identifier).first()
            or User.objects.filter(username__iexact=identifier).first()
        )
        if user:
            attrs[self.username_field] = user.username
        else:
            attrs[self.username_field] = identifier

        data = super().validate(attrs)

        role = normalize_role(self.user)
        permissions = ROLE_FRONTEND_PERMISSIONS.get(role, [])

        # Append complete user metadata directly in authentication response
        data["user"] = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
            "first_name": self.user.first_name or "Admin",
            "last_name": self.user.last_name or "User",
            "role": role,
            "permissions": permissions,
            "avatar": None,
            "is_active": self.user.is_active,
            "is_staff": self.user.is_staff,
            "is_superuser": self.user.is_superuser,
            "date_joined": (
                self.user.date_joined.isoformat()
                if hasattr(self.user, "date_joined") and self.user.date_joined
                else None
            ),
        }
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        role = normalize_role(user)
        # Custom claims embedded in the JWT payload
        token["username"] = user.username
        token["email"] = user.email
        token["role"] = role
        token["first_name"] = user.first_name or "Admin"
        token["last_name"] = user.last_name or "User"
        token["is_staff"] = user.is_staff
        token["is_superuser"] = user.is_superuser
        return token
