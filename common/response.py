from rest_framework import status
from rest_framework.response import Response


def api_response(data=None, message="Success", status_code=status.HTTP_200_OK, success=True, errors=None):
    """
    Standardized API response helper.
    """
    payload = {
        "success": success,
        "status_code": status_code,
        "message": message,
        "data": data if data is not None else {},
    }
    if errors is not None:
        payload["errors"] = errors

    return Response(payload, status=status_code)
