from django import forms

from .models import Address


class AddressForm(forms.ModelForm):
    """Represents form for user address."""

    class Meta:
        """Meta data."""

        model = Address
        exclude = ("user",)
