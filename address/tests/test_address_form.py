"""Contains unit tests suite for address form."""

from django import forms

from address.forms import AddressForm


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
