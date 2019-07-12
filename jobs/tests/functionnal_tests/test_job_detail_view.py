"""COntains all tests for job detail view."""
import pytest

from django.urls import reverse

from jobs.models import JobOffer


@pytest.mark.django_db
class TestJobDetailView:

    job_id = 4
    url = reverse("job_detail", kwargs={"job_id": job_id})

    def test_response_status_code(self, client,
                                  user_teacher_login, db_populated):
        response = client.get(self.url)
        assert response.status_code == 200

    def test_slug(self, client, user_teacher_login, db_populated):
        response = client.get(self.url)
        assert response.status_code == 200

    def test_template_name(self, client, user_teacher_login, db_populated):
        response = client.get(self.url)
        templates = [t.name for t in response.templates]
        assert "jobs/job-detail.html" in templates

    def test_job_offer_in_context(self, client,
                                  user_teacher_login, db_populated):
        response = client.get(self.url)
        job_offer = JobOffer.objects.get(id=self.job_id)
        assert response.context["job_offer"] == job_offer

    def test_user_unauthenticated(self, client, db_populated):
        response = client.get(self.url)
        assert response.status_code == 302

    def test_job_offer_not_exist(self, client,
                                 user_teacher_login, db_populated):
        response = client.get(reverse("job_detail", kwargs={"job_id": 2103}))
        assert response.status_code == 404
