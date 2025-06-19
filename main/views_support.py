from django.shortcuts import render

def support_home(request):
    return render(request, 'support/support_home.html')

def general_inquiries(request):
    return render(request, 'support/general_inquiries.html')

def ai_bot_assistance(request):
    return render(request, 'support/ai_bot_assistance.html')

def live_chat_support(request):
    return render(request, 'support/live_chat_support.html')

def order_status(request):
    return render(request, 'support/order_status.html')

def automation_help(request):
    return render(request, 'support/automation_help.html')

def technical_support(request):
    return render(request, 'support/technical_support.html')

def payments_billing(request):
    return render(request, 'support/payments_billing.html')

def bot_installation(request):
    return render(request, 'support/bot_installation.html')
