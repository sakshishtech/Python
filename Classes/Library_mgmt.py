
from datetime import date, timedelta


class Library:
    loan_days = 7

    def __init__(self):
        self.books = {}

    def add_book(self, book_id, book_name, count):
        self.books[book_id] = {
            "book_name": book_name,
            "available": count
        }

    def borrow_book(self, book_id, borrowed_date=None):
        if book_id not in self.books:
            return "Book not found"

        book = self.books[book_id]

        if book["available"] == 0:
            return "No copies available"

        if borrowed_date is None:
            borrowed_date = date.today()

        book["available"] -= 1

        due_date = borrowed_date + timedelta(days=self.loan_days)

        return f"Borrowed successfully. Due date: {due_date}"

    def return_book(self, book_id):
        if book_id not in self.books:
            return "Book not found"

        book = self.books[book_id]
        book["available"] += 1

        return "Book returned successfully"

    def check_due_date(self, borrowed_date):
        due_date = borrowed_date + timedelta(days=self.loan_days)

        if date.today() > due_date:
            return f"Overdue by {(date.today() - due_date).days} days"

        return f"Due date: {due_date}"
