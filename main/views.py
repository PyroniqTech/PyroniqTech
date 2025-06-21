from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
import traceback
from django.core.management import call_command
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import trustrating
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
        {"name": "Sarah T.", "country": "UAE", "text": "Their automation tools saved me hours daily — 10/10!"},
        {"name": "Ali K.", "country": "Pakistan", "text": "Very helpful and responsive devs."},
        {"name": "John D.", "country": "USA", "text": "Fast, reliable, and secure — highly recommend."},
        {"name": "Ananya M.", "country": "India", "text": "Clean UI and great support from the team."},
        {"name": "Lucas W.", "country": "Germany", "text": "Everything works smoothly. Will use again."},
        {"name": "Mina L.", "country": "Singapore", "text": "Amazing experience! Great quality tools."},
        {"name": "Ahmed S.", "country": "Saudi Arabia", "text": "Saved us tons of manual effort. Great job!"},
        {"name": "Camila R.", "country": "Brazil", "text": "Reliable, fast, and friendly support."},
        {"name": "Kevin B.", "country": "Canada", "text": "Interface is super clean and responsive."},
        {"name": "Isla M.", "country": "UK", "text": "Very professional, loved the results!"},
        {"name": "Farhan Z.", "country": "Pakistan", "text": "Always responsive. Never had issues."},
        {"name": "Tom H.", "country": "Australia", "text": "Excellent support and performance."},
        {"name": "Yuki T.", "country": "Japan", "text": "Secure and reliable — highly recommend."},
        {"name": "Sophia L.", "country": "France", "text": "Tools are super efficient and helpful."},
        {"name": "Mohammad A.", "country": "UAE", "text": "Truly automated and user-friendly."},
        {"name": "Ravi C.", "country": "India", "text": "Loved the responsiveness of the system."},
        {"name": "Anna P.", "country": "Poland", "text": "Quick delivery and clean code."},
        {"name": "Ibrahim K.", "country": "Nigeria", "text": "Great service and smooth experience."},
        {"name": "Emma D.", "country": "USA", "text": "Perfect for startups and agencies."},
        {"name": "Omar F.", "country": "Egypt", "text": "One of the best dev experiences ever."},
        {"name": "Nora H.", "country": "Denmark", "text": "Easy to integrate, loved it!"},
        {"name": "Zara Q.", "country": "Pakistan", "text": "Clean UI and fast support response."},
        {"name": "Luis M.", "country": "Mexico", "text": "100% satisfied with performance."},
        {"name": "Chen Y.", "country": "China", "text": "No downtime and super fast."},
        {"name": "Sami A.", "country": "Jordan", "text": "Very friendly and efficient."},
        {"name": "Fatima R.", "country": "Morocco", "text": "Love the automation tools!"},    
        {"name": "Ethan C.", "country": "USA", "text": "Rock-solid reliability."},
        {"name": "Meera V.", "country": "India", "text": "Never disappointed using PyroniqTech."},
        {"name": "Grace K.", "country": "Kenya", "text": "Real support, real people. Loved it."},
        {"name": "Alexis J.", "country": "South Africa", "text": "Quick turnaround and quality output."},
        {"name": "Bilal M.", "country": "Pakistan", "text": "Highly dependable tools!"},
        {"name": "Sophie G.", "country": "UK", "text": "Intuitive interface and clean setup."},
        {"name": "Tariq L.", "country": "Bangladesh", "text": "Simple, powerful, reliable."},
        {"name": "Jonas E.", "country": "Norway", "text": "Excellent experience overall."},
        {"name": "Layla S.", "country": "Lebanon", "text": "Automation at its finest."},
        {"name": "Musa D.", "country": "Turkey", "text": "Clean, fast and trusted tools."},
        {"name": "Jasmine R.", "country": "USA", "text": "Support team is always ready to help."},
        {"name": "Danish H.", "country": "Pakistan", "text": "Local support with global standards."},
        {"name": "Lina A.", "country": "Indonesia", "text": "Truly game-changing automation."},
        {"name": "Hassan U.", "country": "Pakistan", "text": "Great for growing teams."},
        {"name": "Nina T.", "country": "Thailand", "text": "All-in-one automation tools."},
        {"name": "Ishaan R.", "country": "India", "text": "Just what we needed!"},    
        {"name": "Aaliyah B.", "country": "Malaysia", "text": "Appreciate the professionalism."},
        {"name": "Zain M.", "country": "Pakistan", "text": "Fast delivery and strong backend."},
        {"name": "Olivia C.", "country": "Australia", "text": "Everything just works."},
        {"name": "Rehan K.", "country": "Pakistan", "text": "Great communication and quality."},
        {"name": "Areeba S.", "country": "Pakistan", "text": "Trustworthy and efficient."},
        {"name": "Luca N.", "country": "Italy", "text": "Love the UI and toolset."},
        {"name": "Eva J.", "country": "Germany", "text": "So easy to use and scale."},
        {"name": "Talha Y.", "country": "Pakistan", "text": "Worth every penny!"}
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
