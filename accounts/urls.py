"""Manage routing urls for accounts application."""

from django.urls import path

from . import views


urlpatterns = [
    path("signup/", views.Signup.as_view(), name="signup")
]
