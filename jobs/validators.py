from django.core.exceptions import ValidationError


def size_validator(value):
    """Return Validationerror if file up to 5MB."""
    limit = 5242880
    if value.size > limit:
        raise ValidationError("Le fichier ne doit pas faire plus de 5 Mo.")
