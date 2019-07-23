"""Contains all views for accounts app."""

from django.shortcuts import render
from django.views import View
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site

from accounts.forms import UserCreationForm
from accounts.tokens import account_activation_token


class SignupView(View):
    """Render signup view and call validation form."""

    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    email_template = "emails/signup-validation.html"

    def post(self, request, *args, **kwargs):
        """Manage POST method."""
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user.pk)
            email_context = {"token": token,
                             "uid": uid,
                             "domain": get_current_site(request).domain}
            mail = EmailMessage(
                "Melomnia: Confirmation de l'inscription",
                render_to_string(self.email_template, context=email_context),
                'no-reply@melomnia.fr',
                [user.email]
                )
            mail.content_subtype = "html"
            mail.send()
            return render(request, "accounts/signup-email.html")
        else:
            context = {"form": form}
            return render(request, self.template_name, context)

    def get(self, request):
        """Manage GET method."""
        context = {"form": self.form_class}
        return render(request, self.template_name, context)
