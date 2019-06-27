from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from core.settings import AUTH_USER_MODEL
from .managers import UserManager


class User(AbstractBaseUser):
    """Represents a user."""

    email = models.EmailField(verbose_name="email address",
                              unique=True)
    school_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=10, null=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_school = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        """Check if the user have a specific permission."""
        return True

    def has_module_perms(self, app_label):
        """Check if the user have permissions to view the app 'app_label'."""
        return True

    @property
    def is_staff(self):
        """Check if the user is a member of staff."""
        return self.is_admin


class Address(models.Model):
    """Represents an address linked to a user."""

    user = models.OneToOneField(AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    complement = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=5)
    country = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of an address."""
        return (f"{self.street}, {self.complement}, "
                f"{self.zipcode} {self.city}, {self.country}")
