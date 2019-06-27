"""Contains tests suite for login view."""
import pytest

from django.urls import reverse


@pytest.mark.django_db
class TestLoginView:

    def test_post_method(self, client, django_user_model):
        email, password = "test@django.com", "azertyui"
        user = django_user_model.objects.create(email=email, password=password)
        client.post(reverse("login"), data={"email": email,
                                            "password": password})
        assert user.is_authenticated
