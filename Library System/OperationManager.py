from Admin import *
from User import *

class OperatonManager:
    def __init__(self):
        self.admin = Admin()

    def print_menu(self) -> None:
        print(10*"="+"Program Options"+"="*10)
        options = [
            '1) Add book',
            '2) Print libraty books',
            '3) Print book by prefiks',
            '4) Add User',
            '5) Borrow book',
            '6) Return book',
            '7) Print users borrowed book',
            '8) Print users'
        ]
        print('\n'.join(options))
        return self.get_choice(len(options))
    
    def get_choice(self,num_options):
        """
        Parameter : menerima angka

        Expect: invalid number
        
        """
        msg = f"Enter your choice from 1 to {num_options} \n"
        return input_is_valid(msg,1,num_options)
    
    def add_book(self) -> None:
        book_id = input("Please Enter the book id: \n")
        book_name = input("Please enter tge book name: \n")
        book_quantity = input("Please Enter The book quantuty: \n")
        self.admin.add_book(book_id,book_name,book_quantity)
    
    def print_books(self) -> None:
        print(self.admin.print_all_books())
    
    def search_books(self) -> None:
        query = input("Enter your query: \n")
        print(', '.join(self.admin))

    def run(self) -> None:
        while True:            
            choice = self.print_menu()

            if choice == 2:
                self.print_books()
            else:
                print("By")
                
    