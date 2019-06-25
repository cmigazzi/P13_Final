"""Contains all views for accounts app."""

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm


class Signup(View):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponse("Go to home")

    def get(self, request):
        context = {"form": self.form_class}
        return render(request, self.template_name, context)
