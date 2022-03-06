import mysql.connector
import re
from mysql.connector import errorcode

config = {
    'user': "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "port": 33306, # changed to make it easier for peers to review
    "database": "whatabook",
    "raise_on_warnings": True
}


class Whatabook:
    def __init__(self):
        self.db = mysql.connector.connect(**config)
        self.user = None
        self.user_id = None

    def show_menu(self):
        logged_in = self.user if self.user is not None else "not logged in"
        pattern = re.compile(r"^[0-9]+$")  # numbers in string format only
        selection = input(f"Welcome to What-A-Book!\n"
                          f"Please select an operation: \n"
                          f"   [1] View all Books \n"
                          f"   [2] View Store Locations \n"
                          f"   [3] My Account \n"
                          f"   [4] Exit Program \n"
                          f"-- Logged-in as: {logged_in} \n"
                          f" ")
        if re.match(pattern, selection):
            return selection
        else:
            self.next()
            print(f"{selection}not a valid option")
            self.main()

    def show_books(self):
        query = f"SELECT book_name, author FROM book"
        cursor = self.db.cursor()
        cursor.execute(query)
        books = cursor.fetchall()
        self.next()
        print("-- DIPLAYING BOOKS --")
        for book in books:
            print(f"{book[0]} by {book[1]}")

    def validate_user(self):
        if self.user_id is None:
            pattern = re.compile(r"^[0-9]+$")  # numbers in string format only
            user_id = input("please enter your user ID: ")

            if re.match(pattern, user_id):
                cursor = self.db.cursor()
                query = f"SELECT * FROM user WHERE user.user_id = {int(user_id)}"
                cursor.execute(query)
                result = cursor.fetchall()
                if result:
                    self.user = f"{result[0][1]} {result[0][2]}"
                    self.user_id = int(result[0][0])
                    print("login success!")
                    return True
                else:
                    print("not a valid user")
                    return False
            else:
                print(f"{user_id} is not a valid user ID")
                self.validate_user()

    def show_locations(self):
        cursor = self.db.cursor()
        query = f"SELECT locale FROM store"
        cursor.execute(query)
        stores = cursor.fetchall()
        for store in stores:
            print(f"{store[0]}")

    def show_account_menu(self):
        sub_selection = input(f"Welcome {self.user}! userID: {self.user_id}\n"
                              f"Please select an operation: \n"
                              f"   [1] View Wishlist \n"
                              f"   [2] Add books to Wishlist \n"
                              f"   [3] Exit to Main Menu \n")
        return sub_selection

    def show_wishlist(self):
        cursor = self.db.cursor()
        # cant get query to work without 'SELECT *', cant figure out why
        query = f"SELECT * FROM wishlist w INNER JOIN book b ON w.book_id = b.book_id INNER JOIN user u ON u.user_id = w.user_id WHERE u.user_id = {self.user_id};"
        cursor.execute(query)
        wishlist = cursor.fetchall()
        self.next()
        print("\n-- DISPLAYING WISHLIST --\n")
        i = 1
        for wish in wishlist:
            print(f"[{i}] {wish[4]} by {wish[6]}")
            i += 1

    def add_books_to_wishlist(self):
        cursor = self.db.cursor()
        query = f"SELECT book_id, book_name, details, author FROM book b WHERE b.book_id NOT IN (SELECT book_id FROM wishlist w WHERE w.user_id = {self.user_id});"
        cursor.execute(query)
        books = cursor.fetchall()
        print(f"\n -- SELECT A BOOK TO ADD --\n")
        i = 1
        for book in books:
            print(f"[{i}] {book[1]} by {book[3]}")
            print(f"    about: {book[2]}")
            i += 1
        selected_book = int(input("enter the corresponding number to add the book to your wishlist: "))
        target_book_id = int(books[selected_book - 1][0])
        print(target_book_id)
        cursor = self.db.cursor()
        query = f"INSERT INTO wishlist (user_id, book_id) VALUES ({self.user_id}, {target_book_id})"
        cursor.execute(query)
        self.db.commit()

    def next(self): # tries to make space between interface changes
        for i in range(5):
            print("\n")

    # driver function
    def main(self, selection='0'):
        try:
            if selection == '0':
                selection = self.show_menu()
            if selection == '1':
                self.show_books()
                input("\npress enter key to continue")
                self.next()
                self.main()
            elif selection == '2':
                self.show_locations()
                input("\npress enter key to continue")
                self.next()
                self.main()
            elif selection == '3':
                self.validate_user()
                if self.user:
                    self.next()
                    sub_selection = self.show_account_menu()
                    if sub_selection == '1':
                        self.show_wishlist()
                        input("\npress enter key to continue")
                        self.main('3')
                    elif sub_selection == '2':
                        self.add_books_to_wishlist()
                        self.next()
                        self.show_wishlist()
                        input("\npress enter key to continue")
                        self.next()
                        self.main('3')
                    elif sub_selection == '3':
                        self.next()
                        self.main()
            elif selection == '4':
                print(f"thanks for shopping at What-A-Book! Bye")
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('error authenticating')
                print(error)
            elif error.errno == errorcode.ER_BAD_DB_ERROR:
                print('database does not exist')
            else:
                print(error)
        finally:
            self.db.close()


w = Whatabook()
w.main() # run the driver function