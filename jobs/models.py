from django.db import models

from profiles.models import School


class JobOffer(models.Model):
    """Represent a job offer."""

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    position = models.CharField(max_length=255, null=False)
    half_hour_count = models.PositiveIntegerField()
    contract_type = models.CharField(max_length=255)
    details = models.TextField(null=False)
    apply_email = models.EmailField(null=False)
    limit_date = models.DateField(null=False)
    creation_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """Return string representation."""
        return f"{self.school.user.school_name}: {self.position}"
