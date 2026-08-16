class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book, "added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "removed from the library.")
        else:
            print(book, "not found in the library.")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "has been issued.")
        else:
            print(book, "is not available.")

    def return_book(self, book):
        self.books.append(book)
        print(book, "has been returned.")

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print("-", book)


# Create library
library = Library()

# Add books
library.add_book("Python Programming")
library.add_book("Data Structures")
library.add_book("Java Programming")

library.display_books()

# Issue a book
library.issue_book("Python Programming")

library.display_books()

# Return a book
library.return_book("Python Programming")

library.display_books()