"""Contains tests for JobOffer form."""
from datetime import date

from django import forms

from jobs.forms import JobOfferForm
from jobs.models import JobOffer


def test_form_is_model_form():
    assert issubclass(JobOfferForm, forms.ModelForm)


def test_meta_model_is_joboffer():
    assert JobOfferForm.Meta.model == JobOffer


def test_form_fields():
    assert JobOfferForm.Meta.fields == ("position", "half_hour_count",
                                        "contract_type", "details",
                                        "apply_email", "limit_date")


def test_details_field_class():
    details_field = JobOfferForm().fields["details"]
    assert details_field.widget.attrs["class"] == "materialize-textarea"


def test_half_hour_count_widget():
    assert isinstance(JobOfferForm.declared_fields["half_hour_count"],
                      forms.CharField)


def test_cleaned_half_hour_count():
    data = {"position": "Professeur de trompette",
            "half_hour_count": "6h30",
            "contract_type": "CDI",
            "details": ("Lorem ipsum dolor sit amet, consectetur adipiscing "
                        "elit, sed do eiusmod tempor incididunt ut "
                        "labore et dolore magna aliqua. Ut enim ad minim "
                        "veniam, quis nostrud exercitation ullamco "
                        "laboris nisi ut aliquip ex ea commodo consequat. "
                        "Duis aute irure dolor in reprehenderit in "
                        "voluptate velit esse cillum dolore eu fugiat nulla "
                        "pariatur. Excepteur sint occaecat "
                        "cupidatat non proident, sunt in culpa qui officia "
                        "deserunt mollit anim id est laborum."),
            "apply_email": "emploi@conservatoire.fr",
            "limit_date": date(2019, 11, 2).strftime("%d/%m/%Y")}
    form = JobOfferForm(data=data)
    form.is_valid()
    assert form.cleaned_data["half_hour_count"] == 13
