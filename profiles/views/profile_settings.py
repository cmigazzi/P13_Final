from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.forms.models import model_to_dict

from profiles.forms import SchoolSettingsForm, TeacherSettingsForm
from address.forms import AddressForm
from address.models import Address
from profiles.models import Teacher, School


def profile_settings(request):
    """Return view for user settings."""
    user = request.user
    if user.is_school:
        context = {"profile": user.school}
    elif user.is_teacher:
        context = {"profile": user.teacher}
    return render(request, "profiles/settings.html", context)


class ChangeUserSettings(View):
    """Manage view for change_settings url."""

    address_form_class = AddressForm
    school_settings_form_class = SchoolSettingsForm
    teacher_settings_form_class = TeacherSettingsForm
    template_name = "profiles/change-settings.html"

    def post(self, request, *args, **kwargs):
        """Handle POST method and check forms submission."""
        user = request.user
        if request.user.is_school:
            settings_form = self.school_settings_form_class(
                                request.POST,
                                instance=user.school)
        elif request.user.is_teacher:
            settings_form = self.teacher_settings_form_class(
                                request.POST,
                                instance=user.teacher)
        address_form = self.address_form_class(request.POST,
                                               instance=user.address)

        if settings_form.is_valid() and address_form.is_valid():
            settings_form.save()
            address = address_form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect(reverse("profile_settings"))

        if request.user.is_school:
            context = {"address_form": self.address_form_class,
                       "settings_form": self.school_settings_form_class}
        elif request.user.is_teacher:
            context = {"address_form": self.address_form_class,
                       "settings_form": self.teacher_settings_form_class}
        return render(request, self.template_name, context)

    def get(self, request):
        """Handle GET method and return forms."""
        try:
            address_settings = model_to_dict(request.user.address)
        except Address.DoesNotExist:
            address_settings = {}

        if request.user.is_school:
            try:
                profile_settings = model_to_dict(request.user.school)
            except School.DoesNotExist:
                profile_settings = {}
            context = {"address_form": self.address_form_class(
                                            initial=address_settings),
                       "settings_form": self.school_settings_form_class(
                                            initial=profile_settings)}

        elif request.user.is_teacher:
            try:
                profile_settings = model_to_dict(request.user.teacher)
            except Teacher.DoesNotExist:
                profile_settings = {}
            context = {"address_form": self.address_form_class(
                                            initial=address_settings),
                       "settings_form": self.teacher_settings_form_class(
                                            initial=profile_settings)}
        return render(request, self.template_name, context)
