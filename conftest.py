import pytest

from django.core.management import call_command

from accounts.models import Address


# Database populating
@pytest.fixture(scope="session")
def db_populated(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loadfixtures")


@pytest.fixture()
def user_test(client, django_user_model):
    login_data = {"email": "test@django.com", "password": "azertyui"}
    user = django_user_model.objects.create_user(**login_data)
    user.is_active = True
    user.save()
    client.login(**login_data)


@pytest.fixture()
def user_address():
    return {"street": "50 rue de Genève",
            "complement": "La diamanterie",
            "city": "Sergy",
            "zipcode": "01630",
            "country": "France"}


@pytest.fixture()
def user_teacher(django_user_model, user_address):
    login_data = {"email": "teacher@django.com",
                  "password": "azertyui",
                  "is_teacher": True}

    user = django_user_model.objects.create_user(**login_data)
    user.first_name = "Jean"
    user.last_name = "Coltrain"
    user.phone = "0450421852"
    user.is_active = True
    user.save()
    Address.objects.create(user=user, **user_address)
    return user


@pytest.fixture()
def user_teacher_login(client, user_teacher):
    client.login(email=user_teacher.email, password="azertyui")
    return user_teacher


@pytest.fixture()
def user_school(client, django_user_model, user_address):
    login_data = {"email": "school@django.com",
                  "password": "azertyui",
                  "is_school": True}
    user = django_user_model.objects.create_user(**login_data)
    user.school_name = "Conservatoire de Limonest"
    user.phone = "0450421852"
    user.is_active = True
    user.save()
    Address.objects.create(user=user, **user_address)
    return user


@pytest.fixture()
def user_school_login(client, user_school):
    client.login(email=user_school.email, password="azertyui")
    return user_school


@pytest.fixture()
def teacher_login(client):
    teacher = client.login(email="jeanmi@melomelo.com", password="azertyui")
    return teacher
