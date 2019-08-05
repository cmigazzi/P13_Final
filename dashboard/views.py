"""Contains all views for dashboard app."""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from jobs.models import JobOffer


@login_required()
def dashboard(request):
    """Return dashboard if user is authenticated."""
    user = request.user
    if user.is_school:
        offers = JobOffer.objects.filter(school=user.school)
        context = {"job_offers": offers}
    else:
        context = {}
    return render(request, "dashboard/dashboard.html", context)
