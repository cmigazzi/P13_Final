from django import forms
from django.contrib.auth import get_user_model

from accounts.models import Address

User = get_user_model()


class SettingsForm(forms.ModelForm):
    """Represents form for user settings."""

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    school_name = forms.CharField(required=False)
    phone = forms.CharField(required=False)

    class Meta:
        """Meta data."""

        model = User
        fields = ("email", "first_name", "last_name", "school_name",
                  "phone")


class AddressForm(forms.ModelForm):
    """Represents form for user address."""

    class Meta:
        """Meta data."""

        model = Address
        exclude = ("user",)
