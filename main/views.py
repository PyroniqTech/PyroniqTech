from django.shortcuts import render

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
