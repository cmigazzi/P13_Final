import pytest

from accounts.models import User


@pytest.mark.django_db
class TestUserCreation:
    def test_create_user(self):
        email, password = "test@django.fr", "abcdefg"
        user = User.objects.create_user(email=email, password=password)
        assert user.email == "test@django.fr"

    def test_create_user_with_unormalized_email(self):
        email, password = "test@DJaNGo.fr", "abcdefg"
        user = User.objects.create_user(email=email, password=password)
        assert user.email == "test@django.fr"

    def test_superuser_is_saved(self):
        email, password = "test@django.com", "abcdefg"
        user = User.objects.create_superuser(email=email,
                                             password=password)
        assert User.objects.get(email=email) == user

    def test_create_user_without_email(self):
        password = "abcdefg"
        with pytest.raises(ValueError):
            User.objects.create_user(email=None, password=password)

    def test_create_user_without_password(self):
        email = "test@django.fr"
        user = User.objects.create_user(email=email, password=None)
        assert user.has_usable_password() is False


@pytest.mark.django_db
class TestSuperUserCreation:
    def test_create_superuser(self):
        email, password = "admin@django.com", "poiuytyr"
        User.objects.create_superuser(email=email,
                                      password=password)
        superuser = User.objects.get(email=email)
        assert superuser.email == "admin@django.com"

    def test_create_superuser_is_admin(self):
        email, password = "admin@django.com", "poiuytyr"
        superuser = User.objects.create_superuser(email=email,
                                                  password=password)

        assert superuser.is_admin is True

    def test_superuser_is_saved(self):
        email, password = "admin@django.com", "poiuytyr"
        User.objects.create_superuser(email=email,
                                      password=password)
        superuser = User.objects.get(email=email)
        assert superuser.is_admin is True
