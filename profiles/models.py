from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    """Represents an user profile."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        """Set metadata."""

        abstract = True


class School(Profile):
    """Represents an school profile."""

    school_type = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation."""
        return f"{self.user.school_name}"
