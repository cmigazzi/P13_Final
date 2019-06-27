"""Contains tests suite for views of dashboard."""

from django.urls import reverse


def test_dashboard_unauthtenticated(client):
    response = client.get(reverse("dashboard"), follow=True)
    templates = [t.name for t in response.templates]
    assert "accounts/login-form.html" in templates


def test_dashboard_authenticated(client, user_test):
    response = client.get(reverse("dashboard"))
    templates = [t.name for t in response.templates]
    assert "dashboard/dashboard.html" in templates
