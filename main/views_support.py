from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactSupportForm  # make sure this form exists

def support_home(request):
    if request.method == 'POST':
        form = ContactSupportForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Optional: save to DB if needed

            # Send email (you must configure settings.py properly)
            send_mail(
                subject=f"New Support Message from {name}",
                message=message,
                from_email=email,
                recipient_list=["umairrajput04@gmail.com"],  # 👈 Replace with your real email
                fail_silently=False,
            )

            return redirect('support_home')
    else:
        form = ContactSupportForm()

    return render(request, 'support/support_home.html', {'form': form})


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
