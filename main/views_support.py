from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactSupportForm
from .forms import SupportTicketForm
from .models import SupportTicket
from django.contrib.admin.views.decorators import staff_member_required
from .forms import TicketReplyForm

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
def general(request): return render(request, 'support/general.html')
def ai_bot_help(request): return render(request, 'support/ai_bot_help.html')
def live_chat(request): return render(request, 'support/live_chat.html')
def project_status(request): return render(request, 'support/project_status.html')
def automation_help(request): return render(request, 'support/automation_help.html')
def technical(request): return render(request, 'support/technical.html')
def payment_issues(request): return render(request, 'support/payment_issues.html')
def bot_installation(request): return render(request, 'support/bot_installation.html')


def ticket_submit(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
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
