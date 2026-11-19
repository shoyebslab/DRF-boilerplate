from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom JWT serializer that allows authentication using either
    username or email, and enriches token payload with user profile details.
    """
    def validate(self, attrs):
        username_or_email = attrs.get(self.username_field)

        # Support email-based login
        if "@" in username_or_email:
            user = User.objects.filter(email__iexact=username_or_email).first()
            if user:
                attrs[self.username_field] = user.username

        data = super().validate(attrs)

        # Append user metadata directly in authentication response
        data["user"] = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
            "role": getattr(self.user, "role", "Patient"),
            "is_staff": self.user.is_staff,
            "is_superuser": self.user.is_superuser,
        }
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Custom claims embedded in the JWT payload
        token["username"] = user.username
        token["email"] = user.email
        token["role"] = getattr(user, "role", "Patient")
        token["is_staff"] = user.is_staff
        token["is_superuser"] = user.is_superuser
        return token
