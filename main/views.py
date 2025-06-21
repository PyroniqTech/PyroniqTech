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
