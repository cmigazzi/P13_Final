from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from django.shortcuts import redirect

from jobs.models import JobOffer
from jobs.forms import JobOfferForm


class JobList(ListView):
    """Return view for jobs list."""

    template_name = "jobs/jobs-list.html"
    context_object_name = "jobs"
    queryset = JobOffer.objects.order_by("-creation_date")


class JobDetail(DetailView):
    """Return view for one job offer detail."""

    model = JobOffer


class JobOfferCreate(CreateView):
    """Return view with form to create a job offer."""

    form_class = JobOfferForm
    success_url = "/dashboard/"
    template_name = "jobs/joboffer_form.html"

    def get(self, request, *args, **kwargs):
        """Handle GET method and redirect if user is teacher."""
        self.object = None
        if request.user.is_school:
            return super().render_to_response(super().get_context_data())
        return redirect(reverse("dashboard"))

    def form_valid(self, form):
        """Add user before save in database."""
        self.object = form.save(commit=False)
        self.object.school = self.request.user.school
        self.object.save()
        return super().form_valid(form)
