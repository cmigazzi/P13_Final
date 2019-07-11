"""Contains tests suite for models of profiles app."""
import pytest

from django.db import models
from django.contrib.auth import get_user_model

from profiles.models import Profile, School

User = get_user_model()


class TestProfileModel:

    def test_is_model_subclass(self):
        assert issubclass(Profile, models.Model)

    def test_attributes(self):
        assert hasattr(Profile, "user")


@pytest.mark.django_db
class TestSchoolModel:

    def test_is_profile_subclass(self):
        assert issubclass(School, Profile)

    def test_attributes(self):
        assert hasattr(School, "user")
        assert hasattr(School, "school_type")

    def test_instance(self, user_school):
        school = School(user=user_school, school_type="Conservatoire")
        school.save()

        assert School.objects.get(user=user_school) == school

    def test_string_representation(self, user_school):
        school = School(user=user_school)

        assert school.__str__() == "Conservatoire de Limonest"
