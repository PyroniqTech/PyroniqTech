from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactSupportForm
from .forms import SupportTicketForm
from .models import SupportTicket
from django.contrib.admin.views.decorators import staff_member_required
from .forms import TicketReplyForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.utils.html import strip_tags

def support_home(request):
    categories = [
        ('general', '📄', 'General Inquiries', '100'),
        ('ai_bot_help', '🤖', 'AI Bot Help', '150'),
        ('automation_help', '⚙️', 'Automation Help', '200'),
        ('technical', '🛠', 'Technical Support', '250'),
        ('project_status', '📊', 'Project Status', '300'),
        ('payment_issues', '💳', 'Billing Issues', '350'),
        ('bot_installation', '📦', 'Bot Installation', '400'),
        ('live_chat', '💬', 'Live Chat', '450'),
    ]

    if request.method == 'POST':
        form = ContactSupportForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"New Support Message from {name}",
                message=message,
                from_email=email,
                recipient_list=["umairrajput04@gmail.com"],
                fail_silently=False,
            )
            return redirect('support_home')
    else:
        form = ContactSupportForm()

    return render(request, 'support/support_home.html', {'form': form, 'categories': categories})


# Other views
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


# ✅ Only this view is updated (added send_mail and request.FILES)
def ticket_submit(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save()

            # ✅ Email notification added
            send_mail(
                f'New Ticket: {ticket.ticket_id}',
                f'{ticket.name} submitted a support ticket:\n\n{ticket.message}',
                'support@yourdomain.com',
                ['your-email@example.com'],
                fail_silently=False,
            )

            return render(request, 'support/ticket_submit.html', {
                'ticket_id': ticket.ticket_id,
                'form_submitted': True
            })
    else:
        form = SupportTicketForm()
    return render(request, 'support/ticket_submit.html', {'form': form})


def ticket_status(request):
    ticket_id = request.GET.get('ticket_id')
    ticket = None

    if ticket_id:
        try:
            ticket = SupportTicket.objects.get(ticket_id=ticket_id)
        except SupportTicket.DoesNotExist:
            ticket = None

    return render(request, 'support/ticket_status.html', {'ticket': ticket, 'ticket_id': ticket_id})


@staff_member_required
def ticket_reply_admin(request, ticket_id):
    ticket = SupportTicket.objects.get(ticket_id=ticket_id)
    if request.method == 'POST':
        form = TicketReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.ticket = ticket
            reply.by_admin = True
            reply.save()
            return redirect('ticket_reply_admin', ticket_id=ticket_id)
    else:
        form = TicketReplyForm()
    return render(request, 'support/ticket_reply_admin.html', {'ticket': ticket, 'form': form})


def general_support_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        inquiry_type = request.POST.get('inquiry_type')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        file = request.FILES.get('attachment')

        if not all([name, email, inquiry_type, subject, message]):
            messages.error(request, "Har field bharna zaroori hai.")
            return redirect('general_support')

        email_subject = f"[PyroniqTech Inquiry] {subject}"
        email_body = f"""
You received a new inquiry from PyroniqTech.com:

Name: {name}
Email: {email}
Inquiry Type: {inquiry_type}
Subject: {subject}

Message:
{message}
"""

        try:
            # Email to company inbox
            msg = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email='PyroniqTech Support <support@pyroniqtech.com>',
                to=['umairrajput04@gmail.com'],
                reply_to=[email]
            )
            if file:
                msg.attach(file.name, file.read(), file.content_type)
            msg.send()

            # Auto-reply to visitor
            html_content = f"""
              <div style="font-family: Arial, sans-serif; padding: 20px; background-color: #f9f9f9;">
                <h2 style="color: #0d6efd;">Thank you for contacting PyroniqTech, {name}!</h2>
                <p>We've received your inquiry and will get back to you as soon as possible.</p>
                <hr>
                <p style="font-weight: bold; color: #333;">Your Message:</p>
                <p style="color: #555;">{message}</p>
                <hr>
                <p style="font-size: 14px; color: #777;">This is an automated response. For further assistance, feel free to reply to this email.</p>
                <p style="color: #0d6efd;">– PyroniqTech Support Team</p>
              </div>
            """
            text_content = strip_tags(html_content)
            confirmation_email = EmailMultiAlternatives(
                subject="PyroniqTech – Confirmation of Your Inquiry",
                body=text_content,
                from_email='PyroniqTech Support <support@pyroniqtech.com>',
                to=[email]
            )
            confirmation_email.attach_alternative(html_content, "text/html")
            confirmation_email.send()

            messages.success(request, "Your inquiry has been sent successfully.")
        except Exception as e:
            messages.error(request, "Failed to send email. Please try again later.")

        return redirect('general_support')

    return render(request, 'support/general.html')
