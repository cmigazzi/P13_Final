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

    assert hasattr(User, "is_active")
    assert hasattr(User, "is_admin")
    assert hasattr(User, "is_teacher")
    assert hasattr(User, "is_school")

    assert hasattr(User, "has_perm")
    assert hasattr(User, "has_module_perms")
    assert hasattr(User, "is_staff")


def test_user_creation(django_user_model):
    assert django_user_model == User


def test_string_representation():
    email = "test@django.fr"
    user = User(email=email)
    assert user.__str__() == email


def test_user_manager():
    assert isinstance(User.objects, UserManager)


def test_has_perm():
    perm = "home.can_i"
    assert User().has_perm(perm) is True


def test_has_module_perms():
    app_label = "home"
    assert User().has_module_perms(app_label) is True


def test_is_staff_is_property():
    assert isinstance(type(User()).is_staff, property)


def test_is_staff():
    assert User().is_staff == User().is_admin
