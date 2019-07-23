from django import forms
from django.core.exceptions import ValidationError

from jobs.models import JobOffer


class JobOfferForm(forms.ModelForm):
    """Define form for job offer publishing."""

    def __init__(self, *args, **kwargs):
        """Extend details field widget."""
        super().__init__(*args, **kwargs)
        self.fields["details"].widget.attrs.update(
                                {"class": "materialize-textarea"})
        self.fields["limit_date"].widget.attrs.update(
                                {"class": "datepicker"})

    half_hour_count = forms.CharField(max_length=5, label="Nombre d'heures")

    class Meta:
        """Metadata for form."""

        model = JobOffer
        fields = ("position", "half_hour_count", "contract_type", "details",
                  "apply_email", "limit_date")

    def clean_half_hour_count(self):
        """Convert form hours into half_hour number."""
        hours_input = self.cleaned_data["half_hour_count"]
        if not hours_input[0].isdigit():
            raise ValidationError(
                    "Le nombre d'heures doit être au format 8h00",
                    code="format")
        hours = hours_input.split("h")
        half_hours = int(hours[0])*2
        if hours[1] == "30":
            half_hours += 1
        return half_hours
