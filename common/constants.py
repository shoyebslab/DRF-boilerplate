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


class ResponseMessages:
    SUCCESS = "Operation completed successfully."
    UNAUTHORIZED = "Authentication credentials were not provided or are invalid."
    FORBIDDEN = "You do not have permission to perform this action."
    NOT_FOUND = "Requested resource was not found."
    VALIDATION_ERROR = "One or more validation errors occurred."
    INTERNAL_SERVER_ERROR = "An unexpected error occurred. Please try again later."
