# middleware.py
from django.utils.deprecation import MiddlewareMixin
from urllib.parse import urlencode

class XFrameOptionsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['X-Frame-Options'] = 'SAMEORIGIN'
        return response


class PreviousURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Store the previous URL in the session
        request.session['previous_url'] = request.META.get('HTTP_REFERER', None)
        
        # Continue with the rest of the middleware chain
        response = self.get_response(request)
        
        return response

