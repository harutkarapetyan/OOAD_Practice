from Books import Book
from transaction import Borrower, FictionBook, NonFictionBook


if __name__ == "__main__":
    
    borrower1 = Borrower("Borrower1", "borrower1@examplegmail.com")
    borrower2 = Borrower("Borrower2", "borrower2@examplegmail.com")

    fiction_book = FictionBook()
    non_fiction_book = NonFictionBook()

    book1 = Book("Fiction Book 1", "Fiction Author", "2023-01-01")
    book2 = Book("Non-Fiction Book 1", "Non-Fiction Author", "2023-02-01")

    borrower1.borrow_book(fiction_book, book1)
    borrower2.borrow_book(non_fiction_book, book2)
    borrower1.borrow_book(fiction_book, book2)

    borrower1.return_book(fiction_book, book1)
    borrower2.return_book(non_fiction_book, book2)

    borrower1.view_borrowing_history()
    borrower2.view_borrowing_history()

