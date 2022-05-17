from datetime import date, timedelta

import pytest

from book_mgt.models import Book, BookLoan


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
            email="user@test.com",
            first_name="Test",
            last_name="User",
            password="testpass1234",
        )

    return user


@pytest.fixture
def book(db, author):
    return Book.objects.create(
        code="CD12/35",
        author=author,
        title="David Copperfield",
        year=1849,
        edition="1st Edition",
        available=True,
    )


@pytest.fixture
def book_loan(db, book, user):
    return BookLoan.objects.create(book=book, user=user)


@pytest.fixture
def overdue_book(book_loan, mocker):
    with mocker.patch(book) as overdue:
        overdue.is_overdue.return_value = True
        overdue.days_overdue.return_value = 5
    return overdue
