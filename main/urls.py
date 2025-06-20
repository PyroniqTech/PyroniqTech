from django.urls import path
from . import views
from .views import run_migrations
from .views import create_admin
    

urlpatterns = [
    path('', views.home, name='home'),
    path('automation-tools/', views.automation_tools, name='automation_tools'),
    path('about/', views.about, name='about'),
    path('trust/', views.trust, name='trust'),
    path('career/', views.career, name='career'),
    path('payment/', views.payment, name='payment'),
    path('run-migrations/', run_migrations),
    path('create-admin/', create_admin),
]
