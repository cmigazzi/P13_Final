from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Address(models.Model):
    """Represents an address linked to a user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=255, verbose_name="Rue")
    complement = models.CharField(max_length=255,
                                  verbose_name="complément", null=True)
    city = models.CharField(max_length=255, verbose_name="Ville")
    zipcode = models.CharField(max_length=5, verbose_name="Code postal")
    country = models.CharField(max_length=255, verbose_name="Pays")

    def __str__(self):
        """Return string representation of an address."""
        return (f"{self.street}, {self.complement}, "
                f"{self.zipcode} {self.city}, {self.country}")
