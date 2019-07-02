
from django.shortcuts import render
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model, login

from accounts.tokens import account_activation_token

User = get_user_model()


def activate(request, uid, token):
    """Manage view for link account activation."""
    try:
        user_id = urlsafe_base64_decode(uid).decode()
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        context = {"is_valid_data": False}
    else:
        if account_activation_token.check_token(user.id, token):
            user.is_active = True
            user.save()
            login(request, user)
            context = {"is_valid_data": True}
        else:
            context = {"is_valid_data": False}
    return render(request, "accounts/signup-validation.html", context)
