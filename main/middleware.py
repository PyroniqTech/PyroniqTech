from django.conf import settings
from django.shortcuts import render

# Replace with your actual IP below
ALLOWED_DEV_IP = '127.0.0.1'  # Change this to your real IP later

class UnderDevelopmentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_paths = ['/admin/', '/static/', '/media/']
        user_ip = request.META.get('REMOTE_ADDR')

        if settings.DEBUG:
            if user_ip != ALLOWED_DEV_IP and not any(request.path.startswith(p) for p in allowed_paths):
                return render(request, 'under_development.html')
        return self.get_response(request)
