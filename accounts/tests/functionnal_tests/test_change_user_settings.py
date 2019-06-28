"""Contains tests suite for change settings view."""
import pytest

from django.views import View
from django.urls import reverse
from django.contrib.auth import get_user_model

from accounts.views import ChangeUserSettings
from accounts.forms import AddressForm, SettingsForm

User = get_user_model()


@pytest.fixture()
def teacher_change_settings_data():
    data = {"email": "teacher@testform.com",
            "first_name": "Paul",
            "last_name": "Desmond",
            "phone": "0450421527"}
    return data


@pytest.fixture()
def school_change_settings_data():
    data = {"email": "school@testform.com",
            "school_name": "Conservatoire de Lyon",
            "phone": "0450421852"}
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
        assert self.view.settings_form_class == SettingsForm

    def test_template_name(self):
        assert self.view.template_name == "accounts/change-settings.html"

    def test_get_method_exist(self):
        assert hasattr(ChangeUserSettings, "get")

    def test_url(self, client, user_test):
        response = client.get(self.url)
        assert response.resolver_match.url_name == "change_settings"

    def test_get_method_render_template(self, client, user_test):
        response = client.get(self.url)
        templates = [t.name for t in response.templates]
        assert "accounts/change-settings.html" in templates

    def test_get_status_code(self, client, user_test):
        response = client.get(self.url)
        assert response.status_code == 200

    def testuser_unauthenticated(self, client):
        response = client.get(self.url)
        assert response.status_code == 302

    def test_forms_in_context(self, client, user_test):
        response = client.get(self.url)
        assert response.context["address_form"] == AddressForm
        assert response.context["settings_form"] == SettingsForm

    def test_school_exclude_fields_in_context(self, client, user_test):
        response = client.get(self.url)
        assert response.context["school_exclude_fields"] == ["First name",
                                                             "Last name"]

    def test_post_method(self, client, user_test):
        assert hasattr(ChangeUserSettings, "post")

    def test_teacher_settings_form_submission(self, client,
                                              user_teacher_login,
                                              teacher_change_settings_data,
                                              change_address_data):
        teacher_change_settings_data.update(change_address_data)
        client.post(self.url, data=teacher_change_settings_data)
        user = User.objects.get(id=user_teacher_login.id)
        assert user.email == teacher_change_settings_data["email"]

    def test_school_settings_form_submission(self, client,
                                             user_school_login,
                                             school_change_settings_data,
                                             change_address_data):
        school_change_settings_data.update(change_address_data)
        client.post(self.url, data=school_change_settings_data)
        user = User.objects.get(id=user_school_login.id)
        assert user.email == school_change_settings_data["email"]

    def test_teacher_form_rendering(self, client, user_teacher_login):
        response = client.get(self.url)
        assert "First name" in response.content.decode("utf-8")
        assert "School name" not in response.content.decode("utf-8")

    def test_school_form_rendering(self, client, user_school_login):
        response = client.get(self.url)
        assert "School name" in response.content.decode("utf-8")
        assert "First name" not in response.content.decode("utf-8")
