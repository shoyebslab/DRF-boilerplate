"""
Application-wide constants.
"""

class RoleConstants:
    ADMIN = "Admin"
    MANAGER = "Manager"
    EDITOR = "Editor"
    VIEWER = "Viewer"
    DOCTOR = "Doctor"
    STAFF = "Staff"
    PATIENT = "Patient"

    DEFAULT_ROLES = [
        ADMIN,
        MANAGER,
        EDITOR,
        VIEWER,
        DOCTOR,
        STAFF,
        PATIENT,
    ]


ROLE_FRONTEND_PERMISSIONS = {
    "SUPER_ADMIN": [
        "users:view", "users:create", "users:edit", "users:delete",
        "roles:view", "roles:manage", "permissions:view", "permissions:manage",
        "reports:view", "reports:export", "settings:view", "settings:edit",
    ],
    "ADMIN": [
        "users:view", "users:create", "users:edit",
        "roles:view", "permissions:view",
        "reports:view", "reports:export", "settings:view",
    ],
    "MANAGER": [
        "users:view", "reports:view", "reports:export",
    ],
    "USER": [
        "reports:view",
    ],
    "GUEST": [],
}


def normalize_role(user) -> str:
    """
    Normalizes user role string to match frontend RBAC standard:
    SUPER_ADMIN, ADMIN, MANAGER, USER, GUEST.
    """
    if getattr(user, "is_superuser", False):
        return "SUPER_ADMIN"
    raw_role = (getattr(user, "role", "") or "").upper()
    if raw_role in ["SUPER_ADMIN", "ADMIN", "MANAGER", "USER", "GUEST"]:
        return raw_role
    if getattr(user, "is_staff", False) or raw_role in ["ADMINISTRATOR", "ADMIN"]:
        return "ADMIN"
    return "USER"


class ResponseMessages:
    SUCCESS = "Operation completed successfully."
    UNAUTHORIZED = "Authentication credentials were not provided or are invalid."
    FORBIDDEN = "You do not have permission to perform this action."
    NOT_FOUND = "Requested resource was not found."
    VALIDATION_ERROR = "One or more validation errors occurred."
    INTERNAL_SERVER_ERROR = "An unexpected error occurred. Please try again later."
