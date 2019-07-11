"""Contains tests suite for models of profiles app."""
import pytest

from django.db import models
from django.contrib.auth import get_user_model

from profiles.models import Profile, School, Teacher

User = get_user_model()


class TestProfileModel:

    def test_is_model_subclass(self):
        assert issubclass(Profile, models.Model)

    def test_attributes(self):
        assert hasattr(Profile, "user")
        assert hasattr(Profile, "phone")


@pytest.mark.django_db
class TestSchoolModel:

    def test_is_profile_subclass(self):
        assert issubclass(School, Profile)

    def test_attributes(self):
        assert hasattr(School, "user")
        assert hasattr(School, "school_type")
        assert hasattr(School, "name")

    def test_instance(self):
        user = User.objects.create_user(email="dban@django.com",
                                        password="azertyui",
                                        is_school=True)
        user.is_active = True
        user.save()
        school = School(user=user,
                        school_type="Conservatoire",
                        name="Conservatoire de Limonest",
                        phone="0450421852")
        school.save()

        assert School.objects.get(user=user) == school

    def test_string_representation(self, user_school):
        school = School.objects.get(user=user_school)
        assert school.__str__() == "Ecole VDI"


@pytest.mark.django_db
class TestTeacherModel:

    def test_is_profile_subclass(self):
        assert issubclass(Teacher, Profile)

    def test_attributes(self):
        assert hasattr(Teacher, "user")
        assert hasattr(Teacher, "first_name")
        assert hasattr(Teacher, "last_name")

    def test_instance(self):
        user = User.objects.create_user(email="dbango@django.com",
                                        password="azertyui",
                                        is_teacher=True)
        user.is_active = True
        user.save()
        teacher = Teacher(user=user,
                          first_name="Jean",
                          last_name="Coltrain",
                          phone="0450421852")
        teacher.save()

        assert Teacher.objects.get(user=user) == teacher

    def test_string_representation(self, user_teacher):
        teacher = Teacher.objects.get(user=user_teacher)
        assert teacher.__str__() == "Jean Coltrain"
