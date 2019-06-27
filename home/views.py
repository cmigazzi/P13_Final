from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    """Return the homepage."""
    if request.user.is_authenticated:
        return redirect(reverse("dashboard"))

    context = {"form": AuthenticationForm}
    return render(request, "home/index.html", context)
