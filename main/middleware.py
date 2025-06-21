from django.conf import settings
from django.shortcuts import render
import os

# 👤 Replace this with your actual public IP address
ALLOWED_DEV_IP = '119.155.167.171'

class UnderDevelopmentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_paths = ['/admin/', '/static/', '/media/']

        # 🛡️ Correctly handle IP detection behind Railway proxy
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            user_ip = x_forwarded_for.split(',')[0].strip()
        else:
            user_ip = request.META.get('REMOTE_ADDR')

        # 🐞 Log detected IP to verify in Railway logs
        print(f"Detected User IP: {user_ip}")

        # 🔒 Show 'Under Development' to everyone except whitelisted IP
        if settings.DEBUG:
            if user_ip != ALLOWED_DEV_IP and not any(request.path.startswith(p) for p in allowed_paths):
                return render(request, 'under_development.html')

        return self.get_response(request)
