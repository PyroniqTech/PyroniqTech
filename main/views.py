from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
import traceback
from django.core.management import call_command
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import TrustRating
from django.db.models import Avg
from .models import Review, Rating

def home(request):
    return render(request, 'home.html')

def automation_tools(request):
    return render(request, 'automation_tools.html')

def about(request):
    return render(request, 'about.html')

def trust(request):
    try:
        avg_rating = TrustRating.objects.aggregate(avg=Avg('stars'))['avg']
    except:
        avg_rating = None
    return render(request, 'trust.html', {'average_rating': avg_rating})

def get_average_rating():
    avg = Rating.objects.aggregate(Avg('stars'))['stars__avg']
    return round(avg, 1) if avg else 0

# Utility: Total Ratings
def get_total_ratings():
    return Rating.objects.count()

# ✅ Trust Page View (Real + Fake Reviews)
def trust_page(request):
    real_reviews = Review.objects.all().order_by('-created_at')

    fake_reviews = [  # Your 50-item fake review list here
        {"name": "Sarah T.", "country": "UAE", "text": "Their automation tools saved me hours daily — 10/10!"},
        {"name": "Ali K.", "country": "Pakistan", "text": "Very helpful and responsive devs."},
        {"name": "John D.", "country": "USA", "text": "Fast, reliable, and secure — highly recommend."},
        # ... rest of the 50 you already have ...
    ]

    context = {
        "feedback_submitted": request.method == "POST",
        "average_rating": get_average_rating(),
        "total_ratings": get_total_ratings(),
        "real_reviews": real_reviews,
        "fake_reviews": fake_reviews,
    }
    return render(request, 'trust.html', context)

# ✅ Star Rating Submit View
@csrf_exempt
def submit_rating(request):
    if request.method == 'POST':
        try:
            stars = int(request.POST.get('stars'))
            ip = get_client_ip(request)

            if Rating.objects.filter(ip=ip).exists():
                return JsonResponse({'success': False, 'message': 'Already rated'})

            Rating.objects.create(ip=ip, stars=stars)
            return JsonResponse({'success': True})
        except:
            return JsonResponse({'success': False, 'message': 'Invalid input'})
    return JsonResponse({'success': False})

# ✅ (Optional) Feedback Submit View
# Use if you want to store feedback in DB or email
def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('feedback_name')
        email = request.POST.get('feedback_email')
        message = request.POST.get('feedback_message')
        attachment = request.FILES.get('feedback_attachment')

        # Save to DB or process here if needed

    return redirect('trust')

# ✅ Get User IP Helper
def get_client_ip(request):
    x = request.META.get('HTTP_X_FORWARDED_FOR')
    if x:
        return x.split(',')[0]
    return request.META.get('REMOTE_ADDR')

def career(request):
    return render(request, 'career.html')

def payment(request):
    return render(request, 'payment.html')

def robots_txt(request):
    content = "User-agent: *\nDisallow:"
    return HttpResponse(content, content_type="text/plain")

@require_POST
@csrf_exempt
def submit_rating(request):
    try:
        stars = int(request.POST.get('stars'))
        if 1 <= stars <= 5:
            TrustRating.objects.create(
                stars=stars,
                ip_address=request.META.get('REMOTE_ADDR')
            )
            return JsonResponse({'success': True})
    except:
        pass
    return JsonResponse({'success': False}, status=400)
