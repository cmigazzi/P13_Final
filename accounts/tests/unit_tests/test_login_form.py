from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import LoginForm


def test_is_subclass():
    assert issubclass(LoginForm, AuthenticationForm)


def test_email_label():
    form = LoginForm()
    label = form.fields["username"].label
    assert label == "Adresse email"
