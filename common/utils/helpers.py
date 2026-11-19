import secrets
import string


def get_client_ip(request):
    """
    Extracts the client's real IP address from HTTP headers.
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def generate_random_token(length=32):
    """
    Generates a cryptographically secure URL-safe random string.
    """
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))
