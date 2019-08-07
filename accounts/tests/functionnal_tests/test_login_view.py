"""Contains tests suite for login view."""
import pytest

from django.urls import reverse

from accounts.forms import LoginForm


@pytest.mark.django_db
class TestLoginView:

    url = reverse("accounts:login")

    def test_post_method(self, client, django_user_model):
        email, password = "test@django.com", "azertyui"
        user = django_user_model.objects.create(email=email, password=password)
        client.post(self.url, data={"email": email,
                                    "password": password})
        assert user.is_authenticated

    def test_form(self, client):
        response = client.get(self.url)
        assert isinstance(response.context["form"], LoginForm)
