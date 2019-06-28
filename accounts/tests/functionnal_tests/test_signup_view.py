import pytest

from django.views import View
from django.urls import reverse
from django.contrib.auth import get_user_model

from accounts.forms import UserCreationForm
from accounts.views import SignupView


User = get_user_model()


@pytest.mark.django_db
class TestSignupView:

    url = reverse("signup")
    form_data = {"email": "test@django.com",
                 "user_type": "TEACHER",
                 "password1": "azertyui",
                 "password2": "azertyui"}

    def test_class_is_view(self):
        assert issubclass(SignupView, View)

    def test_attributes(self):
        assert hasattr(SignupView, "form_class")
        assert hasattr(SignupView, "template_name")
        assert hasattr(SignupView, "get")
        assert hasattr(SignupView, "post")

    def test_get_method(self, client):
        response = client.get(self.url)
        assert response.status_code == 200

        templates = [t.name for t in response.templates]
        assert "accounts/signup.html" in templates

    def test_form_in_context(self, client):
        response = client.get(self.url)
        assert response.context["form"] == UserCreationForm

    def test_form_submission(self, client):
        client.post(self.url, self.form_data)
        assert User.objects.get(email=self.form_data["email"])

    def test_invalid_passwords(self, client):
        data = dict(self.form_data)
        data["password2"] = "azerttyy"
        response = client.post(self.url, data)
        form = response.context["form"]
        assert form.errors["password2"]

    def test_invalid_email(self, client):
        data = dict(self.form_data)
        data["email"] = "test@django"
        response = client.post(self.url, data)
        form = response.context["form"]
        assert form.errors["email"]

    def test_redirection_after_signup(self, client):
        response = client.post(self.url, self.form_data)
        assert response.status_code == 302

    def test_redirection_authenticate(self, client):
        response = client.post(self.url, self.form_data, follow=True)
        assert response.resolver_match.url_name == "dashboard"
