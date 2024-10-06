# library_management.py

class Book:
    """Represents a book with a title, an author, and a check-out status."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track if the book is checked out

    def check_out(self):
        """Marks the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Represents a collection of books and manages their check-in and check-out operations."""
    
    def __init__(self):
        self._books = []  # Private list to store books in the library

    def add_book(self, book):
        """Adds a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if available in the library."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return
        print(f"'{title}' is either unavailable or not in the library.")

    def return_book(self, title):
        """Returns a book by title to the library."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' is not in the library.")

    def list_available_books(self):
        """Lists all the books that are currently available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")

