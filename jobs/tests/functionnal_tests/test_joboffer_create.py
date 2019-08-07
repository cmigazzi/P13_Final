"""Contains tests for JobOfferCreateView."""
from datetime import date

from django.views.generic import CreateView
from django.urls import reverse

from jobs.views import JobOfferCreate
from jobs.models import JobOffer
from jobs.forms import JobOfferForm

url = reverse("jobs:create")


def test_is_create_view():
    assert issubclass(JobOfferCreate, CreateView)


def test_form_class():
    assert JobOfferCreate.form_class == JobOfferForm


def test_unathenticated_user(client):
    response = client.get(url)
    assert response.status_code == 302


def test_school_user(client, user_school_login):
    response = client.get(url)
    assert response.status_code == 200


def test_teacher_user(client, user_teacher_login):
    response = client.get(url)
    assert response.status_code == 302


def test_post_method_valid(client, user_school_login):
    data = {"position": "Professeur de trompette",
            "half_hour_count": "6h30",
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
    client.post(url, data=data)
    assert JobOffer.objects.get(school=user_school_login.school,
                                position="Professeur de trompette")
