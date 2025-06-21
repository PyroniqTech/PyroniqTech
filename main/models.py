from django.db import models
import random
import string

# Optional: Auto-generate a unique ticket ID
def generate_ticket_id():
    return 'TKT-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


class SupportTicket(models.Model):
    TICKET_STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    # Automatically generated readable ticket ID (e.g., TKT-A9B4C2D3)
    ticket_id = models.CharField(max_length=40, primary_key=True, default=generate_ticket_id, editable=False)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=TICKET_STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return f"Ticket {self.ticket_id} - {self.status}"


class TicketReply(models.Model):
    ticket = models.ForeignKey(SupportTicket, related_name='replies', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    by_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"Reply to {self.ticket.ticket_id}"


class TrustRating(models.Model):
    stars = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

class Review(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.country})"
