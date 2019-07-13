"""Contains tests for JobOfferCreateView."""
from django.views.generic import CreateView
from django.urls import reverse

from jobs.views import JobOfferCreate
from jobs.models import JobOffer


def test_is_create_view():
    assert issubclass(JobOfferCreate, CreateView)


def test_model():
    assert JobOfferCreate.model == JobOffer


def test_fields():
    assert JobOfferCreate.fields == ["position", "half_hour_count",
                                     "contract_type", "details",
                                     "apply_email", "limit_date"]


def test_unathenticated_user(client):
    response = client.get(reverse("joboffer_create"))
    assert response.status_code == 302


def test_school_user(client, user_school_login):
    response = client.get(reverse("joboffer_create"))
    assert response.status_code == 200


def test_teacher_user(client, user_teacher_login):
    response = client.get(reverse("joboffer_create"))
    assert response.status_code == 302
