from django import forms

from profiles.forms import SchoolSettingsForm, TeacherSettingsForm


class TestSchoolSettingsForm:

    form = SchoolSettingsForm

    def test_is_a_form_instance(self):
        assert issubclass(self.form, forms.ModelForm)

    def test_fields(self):
        assert "name" in self.form.base_fields
        assert "phone" in self.form.base_fields


class TestTeacherSettingsForm:

    form = TeacherSettingsForm

    def test_is_a_form_instance(self):
        assert issubclass(self.form, forms.ModelForm)

    def test_fields(self):
        assert "first_name" in self.form.base_fields
        assert "last_name" in self.form.base_fields
        assert "phone" in self.form.base_fields
