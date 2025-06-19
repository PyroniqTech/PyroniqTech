from django.urls import path
from . import views

urlpatterns = [
    path('', views.support_home, name='support_home'),
    path('general/', views.general_inquiries, name='general_inquiries'),
    path('ai-bot-help/', views.ai_bot_assistance, name='ai_bot_assistance'),
    path('live-chat/', views.live_chat_support, name='live_chat_support'),
    path('project-status/', views.order_status, name='order_status'),
    path('automation-help/', views.automation_help, name='automation_help'),
    path('technical/', views.technical_support, name='technical_support'),
    path('payments/', views.payments_billing, name='payments_billing'),
    path('bot-installation/', views.bot_installation, name='bot_installation'),
]
