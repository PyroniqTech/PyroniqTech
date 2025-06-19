from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('general/', views.general, name='general'),
    path('ai-bot-help/', views.ai_bot_help, name='ai_bot_help'),
    path('live-chat/', views.live_chat, name='live_chat'),
    path('project-status/', views.project_status, name='project_status'),
    path('automation-help/', views.automation_help, name='automation_help'),
    path('technical/', views.technical, name='technical'),
    path('payments/', views.payments, name='payments'),
    path('bot-installation/', views.bot_installation, name='bot_installation'),
]
