import pytest

from django.views import View
from django.urls import reverse
from django.contrib.auth import get_user_model

from accounts.forms import UserCreationForm
from accounts.views import SignupView
from profiles.models import Teacher, School


User = get_user_model()


@pytest.mark.django_db
class TestSignupView:

    url = reverse("accounts:signup")
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

    def test_url_after_valid_signup(self, client):
        response = client.post(self.url, self.form_data)
        templates = [t.name for t in response.templates]
        assert "accounts/signup-email.html" in templates

    def test_email_sending(self, client, mailoutbox):
        client.post(self.url, self.form_data)
        assert len(mailoutbox) == 1

    def test_email_content(self, client, mailoutbox):
        client.post(self.url, self.form_data)
        mail = mailoutbox[0]
        assert mail.subject == "Melomnia: Confirmation de l'inscription"
        assert mail.from_email == "no-reply@melomnia.fr"
        assert list(mail.to) == [self.form_data["email"]]
        assert "Voici le lien" in mail.body

    def test_token_is_in_email(self, client):
        response = client.post(self.url, self.form_data)
        assert response.context["token"]

    def test_uid_is_in_context(self, client):
        response = client.post(self.url, self.form_data)
        assert response.context["uid"]

    def test_validation_link(self, client, mailoutbox):
        response = client.post(self.url, self.form_data)
        link = (f"https://{response.context['domain']}/"
                "accounts/activate/"
                f"{response.context['uid']}/{response.context['token']}")
        mail = mailoutbox[0]
        assert link in mail.body

    def test_techer_profile_creation(self, client):
        client.post(self.url, self.form_data)
        user = User.objects.get(email=self.form_data["email"])
        assert Teacher.objects.get(user=user)

    def test_school_profile_creation(self, client):
        data = dict(self.form_data)
        data["user_type"] = "SCHOOL"
        client.post(self.url, data)
        user = User.objects.get(email=data["email"])
        assert School.objects.get(user=user)
