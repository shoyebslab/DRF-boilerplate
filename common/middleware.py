import logging
import time

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """
    Middleware that logs execution time, HTTP method, and response status.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = round((time.time() - start_time) * 1000, 2)

        # Skip logging static/media requests
        if not request.path.startswith(("/static/", "/media/")):
            logger.info(
                "%s %s - Status: %s - Duration: %sms",
                request.method,
                request.path,
                response.status_code,
                duration,
            )
        return response
