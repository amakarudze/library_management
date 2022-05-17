from django.contrib.auth import get_user_model

import pytest


@pytest.fixture
def new_user(db):
    return get_user_model().objects.create_user(
        email="anna@bspz.com",
        first_name="Test",
        last_name="User",
        password="TestPass12",
    )


@pytest.fixture
def new_superuser(db):
    return get_user_model().objects.create_superuser(
        email="anna@bspz.com",
        first_name="Test1",
        last_name="Test2",
        password="TestPass23",
    )
