import pytest

from accounts.models import User


@pytest.mark.django_db
class TestUserCreation:
    def test_create_user(self):
        email, password = "test@django.fr", "abcdefg"
        user = User.objects.create_user(email=email, password=password)
        assert User.objects.get(email=email) == user

    def test_create_user_with_unormalized_email(self):
        email, password = "test@DJaNGo.fr", "abcdefg"
        user = User.objects.create_user(email=email, password=password)
        assert user.email == "test@django.fr"

    def test_create_user_without_email(self):
        password = "abcdefg"
        with pytest.raises(ValueError):
            User.objects.create_user(email=None, password=password)

    def test_create_user_without_password(self):
        email = "test@django.fr"
        user = User.objects.create_user(email=email, password=None)
        assert user.has_usable_password() is False
