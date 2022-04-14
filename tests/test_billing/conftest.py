import pytest

from billing.models import Fine


@pytest.fixture
def fine(db, overdue_book, book):
    return Fine.objects.create(
        user=overdue_book.user,
        book_loan=overdue_book,
    )
