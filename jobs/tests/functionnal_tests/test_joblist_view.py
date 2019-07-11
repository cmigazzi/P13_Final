"""Contains test for JobList view."""
import pytest

from django.views.generic import ListView
from django.urls import reverse

from jobs.views import JobList
from jobs.models import JobOffer


@pytest.mark.django_db
class TestJobListView:

    url = reverse("jobs")

    def test_is_list_view(self):
        assert issubclass(JobList, ListView)

    def test_template_name(self):
        assert JobList.template_name == "jobs/jobs-list.html"

    def test_context_object_name(self):
        assert JobList.context_object_name == "jobs"

    def test_ordering_list(self, client, db_populated, teacher_login):
        expected = JobOffer.objects.order_by("-creation_date")
        response = client.get(self.url)
        assert list(response.context["jobs"]) == list(expected)
