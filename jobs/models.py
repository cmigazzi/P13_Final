from django.db import models

from profiles.models import School


class JobOffer(models.Model):
    """Represent a job offer."""

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    position = models.CharField(
                    max_length=255,
                    verbose_name="Titre du poste", null=False)
    half_hour_count = models.PositiveIntegerField(
                        verbose_name="Nombre d'heures")
    contract_type = models.CharField(verbose_name="Type de contrat",
                                     max_length=255)
    details = models.TextField(verbose_name="Descriptif du poste", null=False)
    apply_email = models.EmailField(
                verbose_name="Adresse email pour recevoir les candidatures",
                null=False)
    limit_date = models.DateField(verbose_name="Date limite de candidature",
                                  null=False)
    creation_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """Return string representation."""
        return f"{self.school.name}: {self.position}"
