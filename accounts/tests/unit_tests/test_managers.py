from accounts.managers import UserManager


def test_create_user_exist():
    assert hasattr(UserManager, "create_user")


def test_create_superuser_exist():
    assert hasattr(UserManager, "create_superuser")
