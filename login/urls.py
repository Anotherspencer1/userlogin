from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login-home'),
    path("accounts/", include("django.contrib.auth.urls")), 
]