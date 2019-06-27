"""Manage routing urls for accounts application."""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("signup/", views.Signup.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(
                            template_name="accounts/login.html"), name="login")
]
