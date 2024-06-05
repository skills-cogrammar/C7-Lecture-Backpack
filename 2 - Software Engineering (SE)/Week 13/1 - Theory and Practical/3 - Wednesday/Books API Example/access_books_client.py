import requests  # Import the requests library for making HTTP requests
from json import dumps  # Import the dumps function from the json module to convert Python objects to JSON strings

# Define the base URL for the API
url = "http://localhost:5000"
# Define the headers to be used in the requests, specifying the content type as JSON and charset as utf-8
headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}

# Define the endpoint for getting all books
get_all_books = "/books"

# Make a GET request to retrieve all books from the API
books = requests.get(url=f"{url}{get_all_books}", timeout=10)
# Print the list of books retrieved from the API
print(books.json()['books'])

# Store the list of books in a variable
book_items = books.json()['books']

# List of book names to be inserted into the API
insert_books = ["Book 1", "Book 2", "Book 3", "Book 4", "Book 5", "Book 6"]
# List of descriptions corresponding to each book name
insert_description = ["great", "nice", "good", "marvelous", "amazing", "the great one"]

# Iterate over each book name and description pair
for book, description in zip(insert_books, insert_description):
    # Create a payload dictionary with the book name and description
    payload = {"name": book, "description": description}
    # Make a POST request to insert the book into the API
    response = requests.post(url=f"{url}{get_all_books}", data=dumps(payload), headers=headers, timeout=10)
    # Print the response of the POST request
    print(response)

# Define the ID of the book to be retrieved
id = 1
# Make a GET request to retrieve the book with the specified ID
book_id = requests.get(url=f"{url}/books/{id}", timeout=10)
# Print the details of the retrieved book
print(book_id.json())
