from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login-home'),
    path('register/', views.register, name='register'),
]