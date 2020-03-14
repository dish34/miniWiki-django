from django.contrib import admin
from django.urls import path, include
from .views import soup, login_view, index, logout_view, signup_view


urlpatterns = [
    path("", index, name="index"),
    path("login/", login_view, name="login"),
    path("welcome/", soup, name="soup"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
]
