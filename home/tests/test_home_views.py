"""Contains all view tests for home app."""

from django.urls import reverse

from accounts.forms import LoginForm


def test_index_templates(client):
    response = client.get(reverse("home"))
    templates = [t.name for t in response.templates]
    assert "home/index.html" in templates


def test_authentication_form_in_index(client):
    response = client.get(reverse("home"))
    assert response.context["form"] == LoginForm


def test_user_is_authenticated(client, user_test):
    response = client.get(reverse("home"))
    assert response.status_code == 302


def test_templates_when_redirect(client, user_test):
    response = client.get(reverse("home"), follow=True)
    templates = [t.name for t in response.templates]
    assert "dashboard/dashboard.html" in templates
