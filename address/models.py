from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Address(models.Model):
    """Represents an address linked to a user."""

    user = models.OneToOneField(User,
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
