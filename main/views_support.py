from django.shortcuts import render

def support_home(request):
    return render(request, 'support/support_home.html')

def general(request):
    return render(request, 'support/general.html')

def ai_bot_help(request):
    return render(request, 'support/ai_bot_help.html')

def live_chat(request):
    return render(request, 'support/live_chat.html')

def project_status(request):
    return render(request, 'support/project_status.html')

def automation_help(request):
    return render(request, 'support/automation_help.html')

def technical(request):
    return render(request, 'support/technical.html')

def payment_issues(request):
    return render(request, 'support/payment_issues.html')

def bot_installation(request):
    return render(request, 'support/bot_installation.html')
