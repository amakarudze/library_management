from datetime import date, timedelta

from book_mgt.models import Author, Book, BookLoan


def test_author_string_representation(author):
    assert str(author) == "Charles Dickens"


def test_book_string_representation(book):
    assert str(book) == 'David Copperfield' 


def test_book_loan_string_representation(book_loan):
    assert str(book_loan) == f'{book_loan.user} - {book_loan.book}'


def test_book_loan_date_due_overdue_properties(book_loan):
    assert book_loan.date_due - date.today() == timedelta(days=7)
    assert book_loan.is_overdue == False
    assert book_loan.days_overdue == 0
