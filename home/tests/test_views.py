"""Contains all view tests for home app."""

from django.urls import reverse


def test_index_templates(client):
    response = client.get(reverse("home"))
    templates = [t.name for t in response.templates]
    assert "home/index.html" in templates
