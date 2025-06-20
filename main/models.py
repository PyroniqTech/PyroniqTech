from django.db import models
import uuid

class SupportTicket(models.Model):
    TICKET_STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=TICKET_STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return f"{self.subject} - {self.status}"

    ticket_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=20, choices=TICKET_STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket {self.ticket_id} - {self.status}"

class TicketReply(models.Model):
    ticket = models.ForeignKey(SupportTicket, related_name='replies', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    by_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"Reply to {self.ticket.ticket_id}"
