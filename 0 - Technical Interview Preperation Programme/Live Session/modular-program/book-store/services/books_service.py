from file_access import FileAccess

class BookService():

    def __init__(self, file_name):
        self.__data_storage = FileAccess(file_name)

    def get(self, book_id):
        books = self.__data_storage.read()

        for book in books:
            if (book["id"] == book_id):
                return book

    def get_all(self):
        books = self.__data_storage.read()
        return books

    def add_book(self, book_details: dict):
        self.__validate_book_details(book_details)
        
    def __validate_book_details(self, book_details: dict):
        if not book_details.get("id"):
            raise Exception("Book ID is required")
        
        if not book_details.get("title"):
            raise Exception("Book Title is required")

        if not book_details.get("author"):
            raise Exception("Book Author is required")

    def get_book_volume(self):
        books = self.__data_storage.read()
        return len(books)

    def remove(self, book_id): 
        books = self.__data_storage.read()
        return list(filter(lambda id: id != book_id, books))
        


