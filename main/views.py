from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
import traceback
from django.core.management import call_command


def home(request):
    return render(request, 'home.html')

def automation_tools(request):
    return render(request, 'automation_tools.html')

def about(request):
    return render(request, 'about.html')

def trust(request):
    return render(request, 'trust.html')

def career(request):
    return render(request, 'career.html')

def payment(request):
    return render(request, 'payment.html')

def create_admin_user(request):
    username = "maryamumair1612"
    password = "161219Aa"
    email = "umairrajput04@gmail.com"

    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(username=username, password=password, email=email)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return HttpResponse("✅ Superuser created successfully.")
    else:
        return HttpResponse("⚠️ Superuser already exists.")
