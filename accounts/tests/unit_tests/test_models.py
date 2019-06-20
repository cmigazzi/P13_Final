"""Contains all tests for accounts models."""
from django.contrib.auth.models import AbstractBaseUser

from accounts.models import User
from accounts.managers import UserManager


def test_user_model_exists():
    assert User


def test_user_model_inheritance():
    assert issubclass(User, AbstractBaseUser)


def test_username():
    assert User.USERNAME_FIELD == "email"


def test_user_attributes():
    assert hasattr(User, "email")


def test_user_creation(django_user_model):
    assert django_user_model == User


def test_string_representation():
    email = "test@django.fr"
    user = User(email=email)
    assert user.__str__() == email


def test_user_manager():
    assert isinstance(User.objects, UserManager)