from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from .models import JobOffer


class JobList(ListView):
    """Return view for jobs list."""

    template_name = "jobs/jobs-list.html"
    context_object_name = "jobs"
    queryset = JobOffer.objects.order_by("-creation_date")


@login_required()
def job_detail(request, job_id):
    """Return view for one jo offer."""
    try:
        job_offer = JobOffer.objects.get(id=job_id)
    except JobOffer.DoesNotExist:
        raise Http404("L'annonce n'existe pas.")
    context = {"job_offer": job_offer}
    return render(request, "jobs/job-detail.html", context)


class JobDetail(DetailView):
    """Return view for one job offer detail."""

    model = JobOffer
