# ******* You are welcome to use draw.io and download it to your desktop *******
# Download desktop draw.io from https://github.com/jgraph/drawio-desktop/releases

"""     ========= Design Scenario =========
Design a simple Library System for a local library. 
The system should allow librarians to manage book inventory, 
handle borrowing and returning books, and keep track of library members.
"""

"""     -------- Class Diagram --------
•	Design a Class Diagram to represent the structure of the Library System.
    •	Identify classes such as Library, Book, Member, Librarian, BorrowingRecord, 
        and any other relevant entities.
    •	Define attributes and methods for each class.
    •	Consider simple relationships like 
        aggregation (e.g., a Member borrows Books) and 
        association (e.g., a Librarian manages Books).
    •	Provide a brief description explaining the purpose of each class 
        and its role in the Library System.

        -- Class Descriptions:

Library: Represents a library entity with attributes like 
name, address, and a list of books it contains.

Librarian: Represents a librarian entity with attributes like 
name and employee ID. Manages books within the library.

Book: Represents a book entity with attributes like 
title, author, ISBN, genre, and availability status.

Member: Represents a library member entity with attributes like 
name, contact information, and a list of borrowed books.

BorrowingRecord: Represents a borrowing record entity with attributes like 
the book borrowed, the member borrowing it, and the due date.

        -- Relationships:

Librarian-Manages-Book: Represents the 
*association* between a librarian and the books they manage.

Library-Manages-Book: Represents the 
*aggregation* between a library and the books it contains.
Use a hollow diamond shape on the containing class (e.g., Library) 
pointing towards the contained class (e.g., Book)
Label the diamond with a multiplicity (e.g., "0..*")

Member-Borrows-Book: Represents the 
*association* between a member and the books they borrow.

Book-BorrowingRecord: Represents the 
*association* between a book and its borrowing records.

        -- The Diagram: Note - See draw.io file for a better visual
+---------------------------+   +----------------------------------------------------------+
|      Library              |   |     Librarian                                            |
+---------------------------+   +----------------------------------------------------------+
| - name: str               |   | - name: str                                              |
| - address: str            |   | - employee_id: str                                       |
| - books: list             |   |                                                          |
+---------------------------+   +----------------------------------------------------------+
| + add_book(book: Book)    |   | + issue_book(member: Member, book: Book, due_date: Date) |
| + remove_book(book: Book) |   | + return_book(member: Member, book: Book)                |
+---------------------------+   +----------------------------------------------------------+
            |                       |
            | manages               | manages
            |                       |
            v  Diamond              v
+------------------------+      +-------------------------------------------+
|       Book             |      |      Member                               |
+------------------------+      +-------------------------------------------+
| - title: str           |      | - name: str                               |
| - author: str          |      | - contact_info: str                       |
| - isbn: str            |      | - borrowed_books: list                    |
| - genre: str           |      |                                           |
| - available: bool      |      |                                           |   
+------------------------+      +-------------------------------------------+
| + check_availability() |      | + borrow_book(book: Book, due_date: Date) |
+------------------------+      +-------------------------------------------+
            |                       |
            | borrows               | borrows
            |                       |
            v                       v
+-------------------+     +-------------------+
|   BorrowingRecord |     |   BorrowingRecord |
+-------------------+     +-------------------+
| - book: Book      |     | - member: Member  |
| - member: Member  |     | - book: Book      |
| - due_date: Date  |     | - due_date: Date  |
+-------------------+     +-------------------+
"""

"""     -------- CRUD Matrix --------
•	Create a CRUD Matrix to outline the CRUD operations 
    for each class in your Class Diagram. You can use any spreadsheet like
    (MS-Excel, Google Sheets) software.
    to do this.
•	Specify the Create, Read, Update, and Delete operations 
    for classes like Book, Member, and BorrowingRecord.
•	Consider who has permission to perform each operation 
    (e.g., Librarian can add, update, and delete Books, 
    while Members can only read and borrow Books).
•	Provide justification for the access permissions assigned to each operation.

CRUD Matrix for Library System Classes (Basic and Roll-Based Hybrid)
╔═════════════════╦══════════════════════════════════════════════╗
║      Class      ║                  Operations                  ║
╠═════════════════╬══════════════════════════════════════════════╣
║      Book       ║   Create: Librarian                          ║
║                 ║   Read: All                                  ║
║                 ║   Update: Librarian                          ║
║                 ║   Delete: Librarian                          ║
╠═════════════════╬══════════════════════════════════════════════╣
║     Member      ║   Create: Librarian                          ║
║                 ║   Read: All                                  ║
║                 ║   Update: Librarian                          ║
║                 ║   Delete: Librarian                          ║
╠═════════════════╬══════════════════════════════════════════════║
║ BorrowingRecord ║   Create: Librarian                          ║
║                 ║   Read: All                                  ║
║                 ║   Update: Librarian                          ║
║                 ║   Delete: Librarian                          ║
╚═════════════════╩══════════════════════════════════════════════╝

"""
#     -------- MVC Pattern --------

# Model
class Book:
    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.available = True

class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_books(self, keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower()]

    def update_book(self, isbn, **kwargs):
        for book in self.books:
            if book.isbn == isbn:
                for key, value in kwargs.items():
                    setattr(book, key, value)

    def delete_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

class Librarian:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Member:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

# View
class LibraryView:
    def display_books(self, books):
        print("Books in Library:")
        for book in books:
            print(f"Title: {book.title}, Author: {book.author}, "
                  f"ISBN: {book.isbn}, Genre: {book.genre}, "
                  f"Available: {book.available}")

# Controller
class LibraryController:
    def __init__(self, library, view):
        self.library = library
        self.view = view

    def add_book(self, title, author, isbn, genre):
        book = Book(title, author, isbn, genre)
        self.library.add_book(book)

    def search_books(self, keyword):
        books = self.library.search_books(keyword)
        self.view.display_books(books)

    def update_book(self, isbn, **kwargs):
        self.library.update_book(isbn, **kwargs)

    def delete_book(self, isbn):
        self.library.delete_book(isbn)

# Example usage
if __name__ == "__main__":
    # Create model
    library = Library("Local Library", "123 Main St")

    # Create controller and view
    controller = LibraryController(library, LibraryView())
    print("====== Controller Created ======")

    # Add books
    controller.add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Fiction")
    controller.add_book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Classic")
    controller.add_book("The Speed of Trust", "Stephan R. Covey", "9780061121184", "Leadership")

    # Display all books
    print("\n====== Search books after 3 additions ======\n")
    controller.search_books("")  # Empty string to display all books

    # Update book
    controller.update_book("9780743273565", available=False)

    # Display updated book
    print("\n====== Search books after update ======\n")
    controller.search_books("")  # Empty string to display all books

    # Delete book
    controller.delete_book("9780061120084")

    # Display remaining books
    print("\n====== Search books after deletion ======\n")
    controller.search_books("")  # Empty string to display all books

    # Create librarian and member
    librarian = Librarian("John Doe", "LIB001")
    member = Member("Jane Smith", "jane@example.com")

    # Test borrowing and returning books
    book_to_borrow = library.books[0]
    member.borrow_book(book_to_borrow)
    print("\n====== Borrowed book ======\n")
    print(f"{member.name} borrowed: {book_to_borrow.title}")

    book_to_return = library.books[0]
    member.return_book(book_to_return)
    print("\n====== Returned book ======\n")
    print(f"{member.name} returned: {book_to_return.title}")


# Resource below for an advance library management system
# https://www.gleek.io/blog/library-management-system
