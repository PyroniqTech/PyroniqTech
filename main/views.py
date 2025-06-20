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

def run_migrations(request):
    try:
        call_command('migrate')
        return HttpResponse("✅ Migrations completed successfully.")
    except Exception as e:
        return HttpResponse(f"❌ Error: {e}")

def create_admin(request):
    if not User.objects.filter(username='maryamumair1612').exists():
        User.objects.create_superuser(
            username='maryamumair1612',
            email='umairrajput04@gmail.com',
            password='161219Aa'
        )
        return HttpResponse("✅ Admin user created.")
    return HttpResponse("⚠️ Admin already exists.")
