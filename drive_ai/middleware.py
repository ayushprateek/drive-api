import logging

logger = logging.getLogger('django.request')

class APILoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log details of the API call
        logger.info(f"API call: {request.method} {request.path} from {request.META.get('REMOTE_ADDR')}")
        response = self.get_response(request)
        return response
