from utility import *
from Book import *
from User import *


class Admin:
    def __init__(self):
        # konstruktor kosong
        """
        self.books = konstruktor penyimpanan buku
        self.users = konstruktor penyimpanan user
        """
        self.books = []
        self.users = {}

    # menambahkan buku
    def add_book(self,book_id,book_name,book_quantity) -> None:
        for book in self.books:
            if book.id == book_id:
                return print("This bbok is already exist")
            # Book berasal dari class book
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
    
    def add_user(self,user_id,user_name,date_birth):
        for user in self.users:
            if user.id == user_id:
                return print(f"This user already exist !")
        # User berasal dari kelas User
        new_user = User(user_id,user_name,date_birth)
        self.users[new_user] = None
        print("User created successfully !")
    
    # peminjaman buku
    def borrow_book(self,user_name,book_name) -> None:
        found_book = ''.join(self.search_for_book(book_name))
        user_found = False
        # book.quantity artinya mengambil quantity saja tidak yang lain
        available_books = [book for book in self.books if book_name == found_book and book.quantity > 0]
        if not available_books:
            return print("Insufficient quantity!")
        for user,values in self.users.items():
            if user.name.lower() == user_name.lower():
                if values is None:
                    self.users[user] = [book_name]
                else:
                    self.users[user].append(book_name)
                user_found = True
        if not user_found:
            return print('There is no user with this name')
        return print(f"The user {user_name} borrowed {found_book}")
    
    def return_book(self,user_name,book_name) -> None:
        found_book = ''.join(self.search_for_book(book_name))
        user_found = False
        available_books = [book for book in self.books if book.name == found_book]
        if not available_books:
            return print("There is no book with this name")
        available_books[0].quantity += 1
        for user,values in self.users.items():
            if user.name.lower() == user_name.lower():
                if len(values) == 1:
                    self.users[user] = None
                else:
                    self.users[user].remove(book_name)
                user_found = True
        if not user_found:
            return print('There is no user with this name')
        return print(f"The user {user_name} returne {found_book}")
    
    def print_users_borrowed(self):
        user_found = [user for user in self.users if self.users[user] is not None]
        if user_found:
            for user in user_found:
                print(f'The user {user.name} borrowed the books {" and ".join(self.users[user])}')
            else:
                print('There are no users borroed any book')

    def print_all_user(self):
        all_users = [user.name for user in self.users]
        if all_users:
            for user in all_users:
                print(user,end=' ')



