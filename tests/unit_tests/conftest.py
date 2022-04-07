import pytest


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture
def user(db, django_user_model, django_username_field):
    UserModel = django_user_model
    username_field = django_username_field

    try:
        user = UserModel._default_manager.get(**{username_field: "user@test.com"})
    except UserModel.DoesNotExist:
        user = UserModel._default_manager.create_user(
            {"user@test.com", "Test", "User", "testpass1234"}
        )

    return user
