from django import forms
from django.contrib.auth import get_user_model

from .models import School, Teacher

User = get_user_model()


class SchoolSettingsForm(forms.ModelForm):
    """Represents form for user settings."""

    class Meta:
        """Meta data."""

        model = School
        exclude = ("user", )


class TeacherSettingsForm(forms.ModelForm):
    """Represents form for user settings."""

    class Meta:
        """Meta data."""

        model = Teacher
        exclude = ("user",)
