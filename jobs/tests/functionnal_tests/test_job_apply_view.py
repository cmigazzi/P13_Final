"""Contains tests for JobApplyView."""
import pytest

from django.views.generic import FormView
from django.urls import reverse
from django.conf import settings

from jobs.views import JobApplyView
from jobs.forms import JobApplyForm
from jobs.models import JobOffer


URL = reverse("jobs:apply", kwargs={"offer": 4})


def test_is_form_view():
    assert issubclass(JobApplyView, FormView)


def test_form_class():
    assert JobApplyView.form_class == JobApplyForm


def test_template_name():
    assert JobApplyView.template_name == "jobs/apply-form.html"


# ######## GET METHOD ####### #

def test_status_code_unauthenticated(client, db_populated):
    response = client.get(URL)
    assert response.status_code == 302


def test_status_code_as_teacher(client, db_populated, user_teacher_login):
    response = client.get(URL)
    assert response.status_code == 200


def test_status_code_as_school(client, db_populated, user_school_login):
    response = client.get(URL)
    assert response.status_code == 302


def test_job_offer_in_context(client, db_populated, user_teacher_login):
    response = client.get(URL)
    assert response.context["job_offer"] == JobOffer.objects.get(id=4)


# ######### POST METHOD ######### #
@pytest.fixture()
def media_root(tmpdir):
    temp_dir = tmpdir.mkdir("mediafiles")
    settings.MEDIA_ROOT = temp_dir
    return temp_dir


@pytest.fixture()
def post_data(media_root):
    fp = open("jobs/fixtures/test-cv.pdf", "rb")
    post_data = {"motivation": "lorem bla bla bla",
                 "curriculum": fp,
                 }
    return post_data


def test_post_method(client, db_populated, user_teacher_login, post_data):
    response = client.post(URL, post_data, follow=True)
    assert response.resolver_match.url_name == "index"


def test_post_unauthenticated(client, db_populated, post_data):
    response = client.post(URL, post_data, follow=True)
    assert response.resolver_match.url_name == "login"


def test_post_school_user(client, db_populated, user_school_login, post_data):
    response = client.post(URL, post_data, follow=True)
    assert response.resolver_match.url_name == "index"


def test_files_upload(client, db_populated, user_teacher_login,
                      media_root, post_data):
    client.post(URL, post_data)
    assert media_root.listdir()[0].basename == "test-cv.pdf"


def test_files_extension(client, db_populated, user_teacher_login, media_root):
    with open("jobs/fixtures/text-cv.txt", "rb") as fp:
        post_data = {"motivation": "lorem bla bla bla",
                     "curriculum": fp,
                     }
        response = client.post(URL, post_data)
    assert len(response.context["form"].errors) != 0


def test_file_size(client, db_populated, user_teacher_login, media_root):
    with open("jobs/fixtures/big-cv.pdf", "rb") as fp:
        post_data = {"motivation": "lorem bla bla bla",
                     "curriculum": fp,
                     }
        response = client.post(URL, post_data)
    assert len(response.context["form"].errors) != 0


def test_post_method_send_mail(client, db_populated,
                               user_teacher_login,
                               mailoutbox, post_data):
    client.post(URL, post_data)

    assert len(mailoutbox) == 1
    m = mailoutbox[0]
    assert "Jean Coltrain" in m.body
    assert post_data["motivation"] in m.body
    assert user_teacher_login.teacher.phone in m.body
    assert user_teacher_login.email in m.body
