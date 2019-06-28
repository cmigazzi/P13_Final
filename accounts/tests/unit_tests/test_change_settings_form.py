"""Contains unit tests suite for change user settings."""

from django import forms

from accounts.forms import SettingsForm, AddressForm


class TestSettingsForm:

    form = SettingsForm

    def test_is_a_form_instance(self):
        assert issubclass(self.form, forms.ModelForm)

    def test_fields(self):
        assert "first_name" in self.form.base_fields
        assert "last_name" in self.form.base_fields
        assert "school_name" in self.form.base_fields
        assert "phone" in self.form.base_fields


class TestAddressForm:

    form = AddressForm

    def test_is_a_form_instance(self):
        assert issubclass(self.form, forms.ModelForm)

    def test_fields(self):
        fields = [field for field in self.form.base_fields]
        assert "street" in fields
        assert "complement" in fields
        assert "city" in fields
        assert "zipcode" in fields
        assert "country" in fields
