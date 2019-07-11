"""Contains unit tests suite for Adress model."""
from django.db import models

from address.models import Address


def test_model_exist():
    assert issubclass(Address, models.Model)


def test_attributes():
    assert hasattr(Address, "street")
    assert hasattr(Address, "complement")
    assert hasattr(Address, "city")
    assert hasattr(Address, "zipcode")
    assert hasattr(Address, "country")
    assert hasattr(Address, "user")


def test_string_representation(user_teacher):
    assert user_teacher.address.__str__() == ("50 rue de Genève, "
                                              "La diamanterie, "
                                              "01630 Sergy, France")
