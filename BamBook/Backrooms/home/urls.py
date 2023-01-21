from django.urls import path
from home import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path("", views.home, name="home"),
     path("index/", views.login, name="login"),
     path("index/", views.signup, name="signup"),
     path("my_books/", views.my_books, name="my_books"),
     path("index_logined/", views.logout_auth, name="logout"),
]