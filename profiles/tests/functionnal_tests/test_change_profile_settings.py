"""Contains tests suite for change settings view."""
import pytest

from django.views import View
from django.urls import reverse
from django.contrib.auth import get_user_model

from profiles.views import ChangeUserSettings
from profiles.models import Teacher, School
from address.forms import AddressForm
from profiles.forms import SchoolSettingsForm, TeacherSettingsForm

User = get_user_model()


@pytest.fixture()
def teacher_change_settings_data():
    data = {"first_name": "Paul",
            "last_name": "Desmond",
            "phone": "0450421527"}
    return data


@pytest.fixture()
def school_change_settings_data():
    data = {"name": "Conservatoire de Lyon",
            "phone": "0450421852",
            "school_type": "Conservatoire"}
    return data


@pytest.fixture()
def change_address_data():
    return {"street": "50 rue de Lyon",
            "complement": "Urban Eden",
            "city": "Paris",
            "zipcode": "75019",
            "country": "France"}


class TestChangeSettingsView:

    view = ChangeUserSettings()
    url = reverse("change_settings")

    def test_is_a_view_class(self):
        assert issubclass(ChangeUserSettings, View)

    def test_forms_as_attribute(self):
        assert self.view.address_form_class == AddressForm
        assert self.view.school_settings_form_class == SchoolSettingsForm
        assert self.view.teacher_settings_form_class == TeacherSettingsForm

    def test_template_name(self):
        assert self.view.template_name == "profiles/change-settings.html"

    def test_get_method_exist(self):
        assert hasattr(ChangeUserSettings, "get")

    def test_url(self, client, user_teacher):
        response = client.get(self.url)
        assert response.resolver_match.url_name == "change_settings"

    def test_get_method_render_template(self, client, user_teacher_login):
        response = client.get(self.url)
        templates = [t.name for t in response.templates]
        assert "profiles/change-settings.html" in templates

    def test_get_status_code(self, client, user_teacher_login):
        response = client.get(self.url)
        assert response.status_code == 200

    def testuser_unauthenticated(self, client):
        response = client.get(self.url)
        assert response.status_code == 302

    def test_teacher_forms_in_context(self, client, user_teacher_login):
        response = client.get(self.url)
        assert isinstance(response.context["address_form"], AddressForm)
        assert isinstance(response.context["settings_form"],
                          TeacherSettingsForm)

    def test_post_method(self, client, user_test):
        assert hasattr(ChangeUserSettings, "post")

    def test_teacher_settings_form_submission(self, client,
                                              user_teacher_login,
                                              teacher_change_settings_data,
                                              change_address_data):
        teacher_change_settings_data.update(change_address_data)
        client.post(self.url, data=teacher_change_settings_data)
        profile = Teacher.objects.get(user=user_teacher_login)
        assert profile.first_name == teacher_change_settings_data["first_name"]

    def test_school_settings_form_submission(self, client,
                                             user_school_login,
                                             school_change_settings_data,
                                             change_address_data):
        school_change_settings_data.update(change_address_data)
        client.post(self.url, data=school_change_settings_data)
        profile = School.objects.get(user=user_school_login)
        assert profile.name == school_change_settings_data["name"]

    def test_teacher_form_rendering(self, client, user_teacher_login):
        response = client.get(self.url)
        assert "Prénom" in response.content.decode("utf-8")

    def test_school_form_rendering(self, client, user_school_login):
        response = client.get(self.url)
        assert "Nom de l&#39;établissement" in response.content.decode("utf-8")
