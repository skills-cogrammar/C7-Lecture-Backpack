from book_service import BookService
from file_access import FileAccess

class Transactions:
    def __init__(self, file_name):
        self.__data_storage = FileAccess(file_name)
        self.__book_service = BookService("books")

    def lend_book(self, book_id, user_id):
        # check that the book exists in the inventory 
        book_exists = self.__book_service.get(book_id)

        if (not book_exists):
            raise Exception("Book was not found")        

        # Remove book from inventory
        self.__book_service.remove(book_id)   
        self.__write_to_transactions(book_id, user_id)

    def __write_to_transactions(self, book_id, user_id):
        book = self.__book_service.get(book_id)
        
        # Write to transactions 
        transaction = {
            "user_id": user_id,
            "book": book
        }

        self.__data_storage.write(transaction)

        
