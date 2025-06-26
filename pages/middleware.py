from cms.models import Visit
from .utils import detect_source

class VisitLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/admin'):
            source = detect_source(request)
            ip = request.META.get('REMOTE_ADDR')
            Visit.objects.create(source=source, ip_address=ip, user_agent=request.META.get('HTTP_USER_AGENT'))

        return self.get_response(request)
