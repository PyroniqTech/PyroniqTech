from django.conf import settings
from django.shortcuts import render
import os

ALLOWED_DEV_IP = '154.198.117.181'  # Use your actual public IP

class UnderDevelopmentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_paths = ['/admin/', '/static/', '/media/']

        # 🛡️ Get real client IP even behind proxy
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            user_ip = x_forwarded_for.split(',')[0].strip()
        else:
            user_ip = request.META.get('REMOTE_ADDR')

        # 🛠️ Debugging aid: log the detected IP
        print IP: {user_ip}")

        if settings.DEBUG:
            if user_ip != ALLOWED_DEV_IP and not any(request.path.startswith(p) for p in allowed_paths):
                return render(request, 'under_development.html')

        return self.get_response(request)
