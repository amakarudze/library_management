from datetime import date

import pytest

from book_mgt.models import Author


@pytest.fixture
def author(db):
    return Author.objects.create(name="Charles Dickens", about="Some 1800s author")


@pytest.fixture
def author2(db):
    return Author.objects.create(name="Charllote Bronte", about="")
