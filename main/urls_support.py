from django.urls import path
from . import views_support
from .views_support import general_support_view

urlpatterns = [
    path('', views_support.support_home, name='support_home'),
    path('general/', views_support.general, name='general'),
    path('ai-bot-help/', views_support.ai_bot_help, name='ai_bot_help'),
    path('live-chat/', views_support.live_chat, name='live_chat'),
    path('project-status/', views_support.project_status, name='project_status'),
    path('automation-help/', views_support.automation_help, name='automation_help'),
    path('technical/', views_support.technical, name='technical'),
    path('payment/', views_support.payment_issues, name='payment_issues'),
    path('bot-installation/', views_support.bot_installation, name='bot_installation'),
    path('submit-ticket/', views_support.ticket_submit, name='ticket_submit'),
    path('ticket-status/', views_support.ticket_status, name='ticket_status'),
    path('admin-reply/<str:ticket_id>/', views_support.ticket_reply_admin, name='ticket_reply_admin'),
    path('general/', general_support_view, name='general_support'),
]
