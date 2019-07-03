from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    """Overload AuthenticationForm."""

    def __init__(self, *args, **kwargs):
        """Add label for username."""
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Adresse email"
