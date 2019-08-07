"""Contains tests suite for views of dashboard."""
import pytest

from django.urls import reverse


def test_dashboard_unauthtenticated(client):
    response = client.get(reverse("dashboard:index"), follow=True)
    templates = [t.name for t in response.templates]
    assert "accounts/login-form.html" in templates


def test_dashboard_authenticated(client, user_test):
    response = client.get(reverse("dashboard:index"))
    templates = [t.name for t in response.templates]
    assert "dashboard/dashboard.html" in templates


@pytest.mark.django_db
class TestSchoolDashboardView:

    URL = reverse("dashboard:index")

    def test_school_templates(self, client, user_school_login):
        response = client.get(self.URL)
        templates = [t.name for t in response.templates]
        assert "dashboard/school.html" in templates

    def test_job_offer_in_context(self, client,
                                  db_populated, school_login):
        response = client.get(self.URL)
        assert response.context["job_offers"]

    def test_if_job_offers_empty(self, client,
                                 db_populated, user_school_login):
        response = client.get(self.URL)
        assert ("Actuellement, vous n'avez "
                "pas d'annonces actives.") in response.content.decode("utf-8")
