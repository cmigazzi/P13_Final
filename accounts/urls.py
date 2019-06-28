"""Manage routing urls for accounts application."""

from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/",
         auth_views.LoginView.as_view(template_name="accounts/login.html"),
         name="login"),
    path("settings/",
         login_required(views.user_settings),
         name="user_settings"),
    path("change_settings/",
         login_required(views.ChangeUserSettings.as_view()),
         name="change_settings")
]
