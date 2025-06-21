from django.contrib import admin
from .models import SupportTicket, TicketReply
from .models import Review, Rating

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'name', 'email', 'status', 'created_at')
    search_fields = ('ticket_id', 'email', 'name')
    list_filter = ('status',)
    readonly_fields = ('ticket_id', 'created_at')  # ✅ Safe fields


@admin.register(TicketReply)
class TicketReplyAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'by_admin', 'created_at')
    search_fields = ('ticket__ticket_id',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'message', 'created_at')
    search_fields = ('name', 'country', 'message')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('ip', 'stars', 'created_at')
    search_fields = ('ip',)
