from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import LoginForm


def index(request):
    """Return the homepage."""
    if request.user.is_authenticated:
        return redirect(reverse("dashboard"))

    context = {"form": LoginForm}
    return render(request, "home/index.html", context)
