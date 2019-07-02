"""Contains all tests for account activation view."""
import pytest

from django.urls import reverse
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture()
def uid_and_token(client):
    form_data = {"email": "test@django.com",
                 "user_type": "TEACHER",
                 "password1": "azertyui",
                 "password2": "azertyui"}

    email_response = client.post(reverse("signup"),
                                 form_data)
    uid = email_response.context["uid"]
    token = email_response.context["token"]

    return (uid, token)


@pytest.fixture()
def activate_account_client(client, uid_and_token):
    uid, token = uid_and_token
    response = client.get(reverse("activate_account",
                                  kwargs={"uid": uid, "token": token})
                          )
    return {"response": response,
            "uid": uid,
            "token": token}


@pytest.mark.django_db
class TestActivate:

    form_data = {"email": "test@django.com",
                 "user_type": "TEACHER",
                 "password1": "azertyui",
                 "password2": "azertyui"}
    signup_url = reverse("signup")

    def test_response_status_code(self, activate_account_client):
        response = activate_account_client["response"]
        assert response.status_code == 200

    def test_templates(self, activate_account_client):
        response = activate_account_client["response"]
        templates = [t.name for t in response.templates]
        assert "accounts/signup-validation.html" in templates

    def test_user_is_active(self, activate_account_client):
        uid = activate_account_client["uid"]
        user_id = urlsafe_base64_decode(uid).decode()
        user = User.objects.get(id=user_id)
        assert user.is_active

    def test_invalid_uid(self, client, uid_and_token):
        token = uid_and_token[1]
        uid = urlsafe_base64_encode(force_bytes(153))
        response = client.get(reverse("activate_account",
                                      kwargs={"uid": uid, "token": token})
                              )
        assert response.context["is_valid_data"] is False

    def test_context(self, activate_account_client):
        response = activate_account_client["response"]
        assert response.context["is_valid_data"] is True

    def test_invalid_token(self, client, uid_and_token):
        uid = uid_and_token[0]
        token = "57o-aa5f26000dbc02218953"
        response = client.get(reverse("activate_account",
                                      kwargs={"uid": uid, "token": token})
                              )
        assert response.context["is_valid_data"] is False

    def test_user_is_authenticate_after_success(self, activate_account_client):
        response = activate_account_client["response"]
        uid = activate_account_client["uid"]
        user_id = urlsafe_base64_decode(uid).decode()
        user = User.objects.get(id=user_id)
        assert response.context["user"] == user
