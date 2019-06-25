import pytest

from django import forms
from django.contrib.auth import get_user_model
from accounts.forms import UserCreationForm, USER_TYPES_CHOICES

form = UserCreationForm
User = get_user_model()

data_test = {"email": "test@django.com",
             "user_type": "is_teacher",
             "password1": "azertyui",
             "password2": "azertyui"}


def test_class_inheritance():
    assert issubclass(UserCreationForm, forms.ModelForm)


class TestUserTypeField:
    field = form.declared_fields["user_type"]

    def test_user_types_choices(self):
        assert USER_TYPES_CHOICES == [("is_teacher", "Un professeur"),
                                      ("is_school", "Une école")]

    def test_user_type_field(self):
        fields = form.declared_fields
        assert isinstance(fields["user_type"], forms.ChoiceField)

    def test_user_type_widget(self):
        assert isinstance(self.field.widget, forms.Select)

    def test_user_type_choices(self):
        assert self.field.choices == USER_TYPES_CHOICES


class TestPasswordsField:
    fields = [
        form.declared_fields["password1"],
        form.declared_fields["password2"]
    ]

    def test_passwords_field(self):
        for field in self.fields:
            assert isinstance(field, forms.CharField)

    def test_passwords_widget(self):
        for field in self.fields:
            assert isinstance(field.widget, forms.PasswordInput)

    def test_passwords_label(self):
        assert self.fields[0].label == "Mot de passe"
        assert self.fields[1].label == "Confirmation du mot de passe"


def test_email_field():
    fields = [field for field in form.base_fields]
    assert "email" in fields


@pytest.mark.django_db
class TestCleanPasswords:

    def test_method(self):
        assert hasattr(UserCreationForm, "clean_password2")

    def test_form_is_valid(self):
        test_form = form(data=data_test)
        assert test_form.is_valid()

    def test_passwords_dont_match(self):
        data = dict(data_test)
        data["password2"] = "poiuytre"
        test_form = form(data=data)
        assert test_form.is_valid() is False


@pytest.mark.django_db
def test_save_method():
    test_form = form(data=data_test)
    test_form.is_valid()
    test_form.save()
    user = User.objects.get(email="test@django.com")
    assert user.check_password("azertyui")
