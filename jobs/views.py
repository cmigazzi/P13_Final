# from django.shortcuts import render
from django.views.generic import ListView
from .models import JobOffer


class JobList(ListView):
    """Return view for jobs list."""

    template_name = "jobs/jobs-list.html"
    context_object_name = "jobs"
    queryset = JobOffer.objects.order_by("-creation_date")
