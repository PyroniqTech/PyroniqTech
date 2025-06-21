from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('automation-tools/', views.automation_tools, name='automation_tools'),
    path('about/', views.about, name='about'),
    path('trust/', views.trust, name='trust'),
    path('career/', views.career, name='career'),
    path('payment/', views.payment, name='payment'),
    path("robots.txt", views.robots_txt, name="robots_txt"),
    path('submit-rating/', views.submit_rating, name='submit_rating'),
]
