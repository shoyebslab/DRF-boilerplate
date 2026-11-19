import re

from django.core.exceptions import ValidationError


def validate_phone_number(value):
    """
    Validates standard international/national phone number format.
    """
    pattern = r"^\+?[0-9\s\-]{7,20}$"
    if value and not re.match(pattern, value):
        raise ValidationError("Enter a valid phone number.")
    return value


def validate_password_strength(password):
    """
    Ensures password is at least 8 characters long, contains at least one digit
    and one alphabet character.
    """
    if len(password) < 8:
        raise ValidationError("Password must contain at least 8 characters.")
    if not re.search(r"\d", password):
        raise ValidationError("Password must contain at least one digit.")
    if not re.search(r"[a-zA-Z]", password):
        raise ValidationError("Password must contain at least one letter.")
    return password
