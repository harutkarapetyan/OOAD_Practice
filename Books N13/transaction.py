from abc import ABC, abstractmethod
from Brrowers import Borrowing
# Abstract class for library operations
class LibraryOperation(ABC):
    @abstractmethod
    def borrow_book(self, borrower, book):
        pass

    @abstractmethod
    def return_book(self, borrower, book):
        pass

# Concrete classes for different types of books
class FictionBook(LibraryOperation):
    def borrow_book(self, borrower, book):
        borrowing = Borrowing(borrower, book)
        return borrowing

    def return_book(self, borrower, book):
        borrowing = Borrowing(borrower, book)
        borrowing.returned = True

class NonFictionBook(LibraryOperation):
    def borrow_book(self, borrower, book):
        borrowing = Borrowing(borrower, book)
        return borrowing

    def return_book(self, borrower, book):
        borrowing = Borrowing(borrower, book)
        borrowing.returned = True

class Borrower:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.borrowings = []

    def borrow_book(self, book_type, book):
        borrowing = book_type.borrow_book(self, book)
        self.borrowings.append(borrowing)

    def return_book(self, book_type, book):
        for borrowing in self.borrowings:
            if borrowing.book == book and type(borrowing.book) == book_type:
                book_type.return_book(self, book)
                self.borrowings.remove(borrowing)
                break

    def view_borrowing_history(self):
        print(f"Borrowing history for {self.name}:")
        for borrowing in self.borrowings:
            status = "Returned" if borrowing.returned else "Not Returned"
            print(f"- {borrowing.book.title} by {borrowing.book.author} ({type(borrowing.book).__name__}): {status}")
