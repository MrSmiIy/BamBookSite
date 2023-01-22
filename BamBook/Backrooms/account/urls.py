import django.contrib.auth
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('login/', django.contrib.auth.login, name='login'),
    path('logout/', django.contrib.auth.logout, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    # path('logout-then-login/', django.contrib.auth.logout_then_login, name='logout_then_login'),
]