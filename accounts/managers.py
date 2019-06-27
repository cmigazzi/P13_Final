"""Contains manager for user model."""
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Manager of User model."""

    def create_user(self, email, password=None,
                    is_teacher=False, is_school=False):
        """Create a new user."""
        if not email:
            raise ValueError

        user = self.model(
            email=self.normalize_email(email)
            )
        if is_teacher is True:
            user.is_teacher = True
        if is_school is True:
            user.is_school = True

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create a new super user."""
        superuser = self.create_user(email=email, password=password)

        superuser.is_admin = True
        superuser.save(using=self._db)

        return superuser
