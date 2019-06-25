from django import forms

from accounts.models import User

SCHOOL = "SCHOOL"
TEACHER = "TEACHER"
USER_TYPES_CHOICES = [(TEACHER, "Un professeur"),
                      (SCHOOL, "Une école")]


class UserCreationForm(forms.ModelForm):
    """Represents the form for user creation."""

    user_type = forms.ChoiceField(widget=forms.Select,
                                  choices=USER_TYPES_CHOICES)
    password1 = forms.CharField(label="Mot de passe",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmation du mot de passe",
                                widget=forms.PasswordInput)

    class Meta:
        """Link to model."""

        model = User
        fields = ('email',)

    def clean_password2(self):
        """Check if passwords match."""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne sont"
                                        "pas identiques")
        return password2

    def save(self, commit=True):
        """Save the new user in database."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password1"))
        if self.cleaned_data.get("user_type") == TEACHER:
            user.is_teacher = True
        if self.cleaned_data.get("user_type") == SCHOOL:
            user.is_school = True
        if commit:
            user.save()
        return user
