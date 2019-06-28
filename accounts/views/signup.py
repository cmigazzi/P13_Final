"""Contains all views for accounts app."""

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import login, authenticate

from accounts.forms import UserCreationForm


class SignupView(View):
    """Render signup view and call validation form."""

    form_class = UserCreationForm
    template_name = "accounts/signup.html"

    def post(self, request, *args, **kwargs):
        """Manage POST method."""
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect(reverse("home"))
        else:
            context = {"form": form}
            return render(request, self.template_name, context)

    def get(self, request):
        """Manage GET method."""
        context = {"form": self.form_class}
        return render(request, self.template_name, context)
