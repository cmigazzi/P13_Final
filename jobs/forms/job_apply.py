from django import forms


class JobApplyForm(forms.Form):
    """Define Form for job offer applying."""
    motivation = forms.CharField(label="Vos motivations",
                                 widget=forms.Textarea)
    curriculum = forms.FileField(label="Envoyer votre CV")
