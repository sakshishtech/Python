
from datetime import date, timedelta
import pytest
from library import Library


@pytest.fixture
def library():
    lib = Library()
    lib.add_book(101, "Python", 2)
    return lib


def test_add_book(library):
    library.add_book(102, "Java", 3)
    assert library.books[102]["book_name"] == "Java"


def test_borrow_book(library):
    result = library.borrow_book(101, date(2026, 11, 13))

    assert result == "Borrowed successfully. Due date: 2026-11-20"
    assert library.books[101]["available"] == 1


def test_no_copies_available(library):
    library.borrow_book(101)
    library.borrow_book(101)

    assert library.borrow_book(101) == "No copies available"


def test_return_book(library):
    library.borrow_book(101)
    library.return_book(101)

    assert library.books[101]["available"] == 2


def test_due_date(library):
    borrowed_date = date.today() - timedelta(days=10)

    result = library.check_due_date(101, borrowed_date)

    assert result == "Overdue by 3 days"
