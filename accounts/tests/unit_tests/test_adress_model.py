"""Contains unit tests suite for Adress model."""
import pytest

from django.db import models

from accounts.models import Address


@pytest.fixture()
def test_address(django_user_model):
    user = django_user_model.objects.create(email="test@django.com",
                                            password="azertyui")

    return {
        "user": user,
        "street": "50 rue de Genève",
        "complement": "La diamanterie",
        "city": "Sergy",
        "zipcode": "01630",
        "country": "France"
    }


def test_model_exist():
    assert issubclass(Address, models.Model)


def test_attributes():
    assert hasattr(Address, "street")
    assert hasattr(Address, "complement")
    assert hasattr(Address, "city")
    assert hasattr(Address, "zipcode")
    assert hasattr(Address, "country")
    assert hasattr(Address, "user")


def test_string_representation(test_address):
    address = Address(**test_address)
    assert address.__str__() == ("50 rue de Genève, "
                                 "La diamanterie, 01630 Sergy, France")
