"""Contains tests suite for user settings view."""

from django.urls import reverse


class TestUserSettingsView:

    url = reverse("user_settings")

    def test_status_code(self, client, user_test):
        response = client.get(self.url)
        assert response.status_code == 200

    def test_templates(self, client, user_test):
        response = client.get(self.url)
        templates = [t.name for t in response.templates]
        assert "accounts/settings.html" in templates

    def test_user_unauthenticated(self, client):
        response = client.get(self.url)
        assert response.status_code == 302

    def test_templates_with_teacher_user(self, client, user_teacher_login):
        response = client.get(self.url)
        assert "Prénom: Jean" in response.content.decode("utf-8")

    def test_templates_with_school_user(self, client, user_school_login):
        response = client.get(self.url)
        assert ("Nom de l'établissement: "
                "Conservatoire de Limonest") in response.content.decode(
                                                                    "utf-8")

    def test_templates_with_address(self, client, user_teacher_login):
        response = client.get(self.url)
        assert ("50 rue de Genève, "
                "La diamanterie, 01630 Sergy, "
                "France") in response.content.decode("utf-8")
