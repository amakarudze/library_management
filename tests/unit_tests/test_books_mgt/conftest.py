from datetime import date

import pytest

from book_mgt.models import Author, BookLoan


@pytest.fixture
def author(db):
    return Author.objects.create(
        name='Charles Dickens',
        about='Some 1800s author'
    )


@pytest.fixture
def author2(db):
    return Author.objects.create(
        name='Charllote Bronte',
        about=''
    )


@pytest.fixture
def book_loan(db, book, user):
    return BookLoan.objects.create(
        book=book,
        user=user,
        date_loaned_out=date.today()
    )
