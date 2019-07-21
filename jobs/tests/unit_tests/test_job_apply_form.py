"""Contains tests for JobApplyForm."""
from django import forms

from jobs.forms import JobApplyForm


def test_is_model_form():
    assert issubclass(JobApplyForm, forms.Form)


def test_motivation_field():
    field = JobApplyForm.base_fields["motivation"]
    assert isinstance(field, forms.CharField)
    assert field.label == "Vos motivations"
    assert isinstance(field.widget, forms.widgets.Textarea)


def test_curriculum_field():
    field = JobApplyForm.base_fields["curriculum"]
    assert isinstance(field, forms.FileField)
    assert field.label == "Joignez votre CV"


def test_motivation_field_class():
    motivation_field = JobApplyForm().fields["motivation"]
    assert motivation_field.widget.attrs["class"] == "materialize-textarea"
