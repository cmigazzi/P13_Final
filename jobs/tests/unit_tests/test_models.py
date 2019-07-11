"""Contains tests for models of jobs app."""
from datetime import date

import pytest

from django.db import models

from jobs.models import JobOffer


@pytest.fixture
def job_offer(user_school):
    offer = {"school": user_school.school,
             "position": "Professeur de trompette",
             "half_hour_count": 10,
             "contract_type": "CDI",
             "details": ("Lorem ipsum dolor sit amet, consectetur adipiscing "
                         "elit, sed do eiusmod tempor incididunt ut "
                         "labore et dolore magna aliqua. Ut enim ad minim "
                         "veniam, quis nostrud exercitation ullamco "
                         "laboris nisi ut aliquip ex ea commodo consequat. "
                         "Duis aute irure dolor in reprehenderit in "
                         "voluptate velit esse cillum dolore eu fugiat nulla "
                         "pariatur. Excepteur sint occaecat "
                         "cupidatat non proident, sunt in culpa qui officia "
                         "deserunt mollit anim id est laborum."),
             "apply_email": "emploi@conservatoire.fr",
             "limit_date": date(2019, 11, 2).strftime("%d/%m/%Y")}
    return offer


class TestJobOffer:

    def test_is_models_subclass(self):
        assert issubclass(JobOffer, models.Model)

    def test_attributes(self):
        assert hasattr(JobOffer, "school")
        assert hasattr(JobOffer, "position")
        assert hasattr(JobOffer, "half_hour_count")
        assert hasattr(JobOffer, "contract_type")
        assert hasattr(JobOffer, "details")
        assert hasattr(JobOffer, "apply_email")
        assert hasattr(JobOffer, "limit_date")
        assert hasattr(JobOffer, "creation_date")
        assert hasattr(JobOffer, "is_active")

    def test_string_representation(self, job_offer):
        offer = JobOffer(**job_offer)
        assert offer.__str__() == ("Ecole VDI: "
                                   "Professeur de trompette")
