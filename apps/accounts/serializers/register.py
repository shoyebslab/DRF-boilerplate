from django.contrib.auth import get_user_model
from rest_framework import serializers

from common.validators import validate_password_strength, validate_phone_number

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password_strength],
        style={"input_type": "password"}
    )
    password_confirm = serializers.CharField(
        write_only=True,
        required=True,
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
            "password_confirm",
            "phone",
            "first_name",
            "last_name",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError({"password_confirm": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        from apps.accounts.services.auth_service import register_user
        validated_data.pop("password_confirm")
        return register_user(validated_data)
