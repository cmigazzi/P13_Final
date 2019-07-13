from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    """Represents an user profile."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, verbose_name="Numéro de téléphone",
                             null=True)

    class Meta:
        """Set metadata."""

        abstract = True


class School(Profile):
    """Represents an school profile."""

    name = models.CharField(max_length=255,
                            verbose_name="Nom de l'établissement",
                            null=True)
    school_type = models.CharField(max_length=255, verbose_name="Type d'école")

    def __str__(self):
        """Return string representation."""
        return f"{self.name}"


class Teacher(Profile):
    """Represents an school profile."""

    first_name = models.CharField(max_length=255,
                                  verbose_name="Prénom", null=True)
    last_name = models.CharField(max_length=255, verbose_name="Nom", null=True)

    def __str__(self):
        """Return string representation."""
        return f"{self.first_name} {self.last_name}"
