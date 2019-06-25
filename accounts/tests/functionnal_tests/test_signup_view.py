import pytest

from django.views import View
from django.urls import reverse
from django.contrib.auth import get_user_model

from accounts.forms import UserCreationForm
from accounts.views import Signup


User = get_user_model()


@pytest.mark.django_db
class TestSignupView:

    def test_class_is_view(self):
        assert issubclass(Signup, View)

    def test_attributes(self):
        assert hasattr(Signup, "form_class")
        assert hasattr(Signup, "template_name")
        assert hasattr(Signup, "get")
        assert hasattr(Signup, "post")

    def test_get_method(self, client):
        response = client.get(reverse("signup"))
        assert response.status_code == 200

        templates = [t.name for t in response.templates]
        assert "accounts/signup.html" in templates

    def test_form_in_context(self, client):
        response = client.get(reverse("signup"))
        assert response.context["form"] == UserCreationForm

    def test_form_submission(self, client):
        data = {"email": "test@django.com",
                "user_type": "TEACHER",
                "password1": "azertyui",
                "password2": "azertyui"}
        client.post(reverse("signup"), data)
        assert User.objects.get(email=data["email"])

    def test_invalid_passwords(self, client):
        data = {"email": "test@django.com",
                "user_type": "TEACHER",
                "password1": "azertyui",
                "password2": "azerttyy"}
        response = client.post(reverse("signup"), data)
        form = response.context["form"]
        assert form.errors["password2"]

    def test_invalid_email(self, client):
        data = {"email": "test@django",
                "user_type": "TEACHER",
                "password1": "azertyui",
                "password2": "azerttyui"}
        response = client.post(reverse("signup"), data)
        form = response.context["form"]
        assert form.errors["email"]
