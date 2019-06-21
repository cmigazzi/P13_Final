from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    """Represents a user."""

    email = models.EmailField(verbose_name="email address",
                              unique=True)
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
