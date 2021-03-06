from django import forms
from django.core.validators import FileExtensionValidator

from jobs.validators import size_validator


class JobApplyForm(forms.Form):
    """Define Form for job offer applying."""

    motivation = forms.CharField(label="Vos motivations",
                                 widget=forms.Textarea(
                                     attrs={"class": "materialize-textarea"}))
    curriculum = forms.FileField(label="Joignez votre CV",
                                 validators=[FileExtensionValidator(["pdf"]),
                                             size_validator])
