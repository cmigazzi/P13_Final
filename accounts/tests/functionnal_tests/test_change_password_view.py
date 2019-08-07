from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

url = reverse("accounts:change_password")


def test_url(client, user_teacher_login):
    response = client.get(url)
    assert "change_password" in response.resolver_match.url_name


def test_status_code_user_unauthenticated(client):
    response = client.get(url)
    assert response.status_code == 302


def test_login_redirection_user_unauthenticated(client):
    response = client.get(url, follow=True)
    assert "login" in response.resolver_match.url_name


def test_template_name(client, user_teacher_login):
    response = client.get(url)
    templates = [t.name for t in response.templates]
    assert "accounts/change-password.html" in templates


def test_form_submission(client, user_teacher_login):
    data = {"old_password": "azertyui",
            "new_password1": "qsdfghjk",
            "new_password2": "qsdfghjk"}
    client.post(url, data=data)
    user = User.objects.get(id=user_teacher_login.id)
    assert user.check_password("qsdfghjk") is True
