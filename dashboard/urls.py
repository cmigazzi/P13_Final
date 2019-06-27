"""Manage urls for dashboard app."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard")
]
