# Import necessary modules from Flask and Flask-SQLAlchemy.
from flask import Flask, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


# DB Connections for SQLAlchemy
engine = create_engine("sqlite:///book_store.sqlite3")
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


# Create a new Flask application.
app = Flask(__name__)

# Custom function
def calculate_age(creation_year:str) -> int:
    """
    Calculate the age of the book inserted
    Warning: 2024 is hardcoded. This should be dynamic.
    """
    return 2024 - int(creation_year)

# Define a Book model using SQLAlchemy.
class Book(Base):
    __tablename__ = "book"
    # Define the primary key and other columns for the Book model.
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(120))
    age = Column(Integer, nullable=False)

    # Define a string representation for the Book model.
    def __repr__(self):
        return f"{self.name}"

# Perform database migration and create all tables.
with app.app_context():
    Base.metadata.create_all(bind=engine)

# Define a route for the root URL of the application.
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Define a route to retrieve all books from the database.
@app.route("/books")
def get_all_books():
    # Retrieve all books from the database.
    books = Book.query.all()
    # Initialize an empty list to store book data.
    output = []
    # Iterate over each book and create a dictionary of book data.
    for book in books:
        book_data = {"name": book.name, "description": book.description, "age": book.age}
        output.append(book_data)
    # Return the list of book data.
    return {"books": output}

# Define a route to retrieve a book by its ID.
@app.route("/books", methods=['GET'])  # Default route
def get_book_by_id(id):
    # Retrieve a book by its ID from the database.
    book = Book.query.get_or_404(id)
    # Return the book data.
    return {"name": book.name, "description": book.description, "age": book.age}

# Define a route to add a new book to the database.
@app.route("/books", methods=["POST"])
def add_book():
    # Get the age of the new book from its creation year
    book_age = calculate_age(request.json["year"])
    # Create a new book from the JSON data.
    book = Book(name=request.json["name"], 
                description=request.json["description"],
                age = book_age)
    # Add the book to the database session.
    db_session.add(book)
    # Commit the changes to the database.
    db_session.commit()
    # Return the ID of the newly added book.
    return {"id": book.id}

# Define a route to delete a book by its ID.
@app.route("/books/<id>", methods=["DELETE"])
def delete_book_by_id(id):
    # Retrieve a book by its ID from the database.
    book = Book.query.filter(Book.id == id)
    # Delete the book from the database.
    book.delete()
    # Commit the changes to the database.
    db_session.commit()
    # Return a success message.
    return {"Message": f"Book with id {id} deleted"}

# Define a route to update a book by its ID.
@app.route("/books/<id>", methods=["PUT"])
def update_book_by_id(id):
    # Retrieve a book by its ID from the database.
    book = Book.query.filter(Book.id == id).first()
    # Get the updated book name and description from the JSON data.
    name = request.json['name']
    description = request.json['description']
    # Update the book with the new data.
    book.name = name
    book.description = description
    # Commit the changes to the database.
    db_session.commit()
    # Return a success message.
    return {"Message": f"Book with id {id} updated"}

# Run the application in debug mode if it is the main module.
if __name__ == '__main__':
    app.run(debug=True)
