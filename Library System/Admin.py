from utility import *
from Book import *
from User import *


class Admin:
    def __init__(self):
        self.books = []
        self.user = {}

    # menambahkan buku
    def add_book(self,book_id,book_name,book_quantity) -> None:
        for book in self.books:
            if book.id == book_id:
                return print("This bbok is already exist")
        new_book = Book(book_id,book_name,book_quantity)
        self.books.append(new_book)
        print("Book is added successfully")
    
    # print seluruh buku
    def print_all_books(self) -> str:
        list_of_books = []
        for book in self.books:
            list_of_books.append(book.name)
        if not list_of_books:
            return f"There are no books"
        return ", ".join(list_of_books)

    # mencari sebuah buku
    def search_for_book(self,query) -> str:
        found_books = [book.name for book in self.books if book.name[:len(query)].upper() == query.upper()]
        if not found_books:
            return f"No book found"
        return found_books
