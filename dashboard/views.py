"""Contains all views for dashboard app."""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def dashboard(request):
    """Return dashboard if user is authenticated."""
    return render(request, "dashboard/dashboard.html")
