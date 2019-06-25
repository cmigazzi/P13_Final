"""Contains all views for accounts app."""

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from accounts.forms import UserCreationForm


class Signup(View):
    """Render signup view and call validation form."""

    form_class = UserCreationForm
    template_name = "accounts/signup.html"

    def post(self, request, *args, **kwargs):
        """Manage POST methof."""
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Go to home")
        else:
            context = {"form": form}
            return render(request, self.template_name, context)

    def get(self, request):
        """Manage GET method."""
        context = {"form": self.form_class}
        return render(request, self.template_name, context)
