from django.conf import settings
from django.shortcuts import render
import os

# Replace with your actual IP below
ALLOWED_DEV_IP = '154.198.117.181'  # Change this to your real IP later

class UnderDevelopmentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_paths = ['/admin/', '/static/', '/media/']
        user_ip = request.META.get('REMOTE_ADDR')

        if settings.DEBUG:
            if user_ip != ALLOWED_DEV_IP and not any(request.path.startswith(p) for p in allowed_paths):
                print("\n\nTEMPLATE DIR CHECK:", os.listdir(os.path.join(settings.BASE_DIR, 'main', 'templates')), "\n\n")
                return render(request, 'under_development.html')

        return self.get_response(request)
