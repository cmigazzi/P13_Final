from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    """Represents a user."""

    email = models.EmailField(verbose_name="email address",
                              unique=True)

    USERNAME_FIELD = "email"

    objects = UserManager()
