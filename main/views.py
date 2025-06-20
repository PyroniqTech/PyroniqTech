from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
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

def create_superuser_easy(request):
    try:
        username = "maryamumair1612"
        password = "161219Aa"
        email = "umairrajput04@gmail.com"

        if User.objects.filter(username=username).exists():
            return HttpResponse("⚠️ User 'maryamumair1612' already exists.")

        User.objects.create_superuser(username=username, email=email, password=password)
        return HttpResponse("✅ Superuser created successfully! You can now log in at /admin/")

    except Exception as e:
        return HttpResponse(f"❌ Internal Server Error: {str(e)}")

def run_migrations(request):
    try:
        call_command('migrate')
        return HttpResponse("✅ Migrations ran successfully.")
    except Exception as e:
        return HttpResponse(f"❌ Migration error: {str(e)}")
