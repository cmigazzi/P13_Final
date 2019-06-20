"""Contains manager for user model."""
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Manager of User model."""

    def create_user(self, email, password=None):
        """Create a new user."""
        if not email:
            raise ValueError

        user = self.model(
            email=self.normalize_email(email)
            )
        user.set_password(password)
        user.save(using=self._db)

        return user
