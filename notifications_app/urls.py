from django.urls import path

from . import views

urlpatterns = [
    path('email-settings/', views.email_settings, name='email_settings'),
]
