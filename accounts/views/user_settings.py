from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from accounts.forms import AddressForm, SettingsForm


def user_settings(request):
    """Return view for user settings."""
    return render(request, "accounts/settings.html")


class ChangeUserSettings(View):
    """Manage view for change_settings url."""

    address_form_class = AddressForm
    settings_form_class = SettingsForm
    template_name = "accounts/change-settings.html"

    def post(self, request, *args, **kwargs):
        """Handle POST method and check forms submission."""
        user = request.user
        settings_form = self.settings_form_class(request.POST, instance=user)
        address_form = self.address_form_class(request.POST,
                                               instance=user.address)
        if settings_form.is_valid() and address_form.is_valid():
            settings_form.save()
            address = address_form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect(reverse("user_settings"))

        context = {"address_form": self.address_form_class,
                   "settings_form": self.settings_form_class}
        return render(request, self.template_name, context)

    def get(self, request):
        """Handle GET method and return forms."""
        context = {"address_form": self.address_form_class,
                   "settings_form": self.settings_form_class,
                   "school_exclude_fields": ["First name", "Last name"]}
        return render(request, self.template_name, context)
