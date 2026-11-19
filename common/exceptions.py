import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
    Standardizes DRF error responses across the application:
    {
        "success": false,
        "status_code": 400,
        "message": "...",
        "errors": { ... }
    }
    """
    response = exception_handler(exc, context)

    if response is not None:
        message = "Validation failed or request could not be processed."
        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            message = "Authentication credentials were not provided or are invalid."
        elif response.status_code == status.HTTP_403_FORBIDDEN:
            message = "You do not have permission to perform this action."
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            message = "The requested resource was not found."
        elif response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED:
            message = "Method not allowed on this endpoint."
        elif response.status_code == status.HTTP_429_TOO_MANY_REQUESTS:
            message = "Request was throttled. Please try again later."

        data = {
            "success": False,
            "status_code": response.status_code,
            "message": message,
            "errors": response.data,
        }
        response.data = data
        return response

    # Handle unhandled server exceptions (500)
    logger.exception("Unhandled server exception: %s", exc, exc_info=context.get("request"))
    return Response(
        {
            "success": False,
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "Internal server error. Please contact system administrator.",
            "errors": str(exc) if hasattr(exc, "message") else "Server error",
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
