# Python projects
# 001 - LMS  (v1)
# My first python project deals with an application of Library Management System.
"""
  Which has 4 prominent actions namely:
  1. Display Books (used to display the books available in the library)
  2. Issue Book (used to issuing and monitoring the issue of a book available in the library)
  3. Add Book (used to add a book to the already existing library similar to updating the library catalog)
  4. Return Book (used to return the issued book back to the library)
"""
# I will try to keep updating this Library Management System as time passes on.


import datetime
import os
os.getcwd()

class LMS:
    """
    This class has 4 modules which are used to keep record of the books in the library.
    The modules: 'Display Books', 'Issue Book', 'Add Book', 'Return Book'
    'library_catalog' should be txt file. 'library_name' should be string.
    """

    def __init__(self, library_catalog, library_name):
        self.library_catalog = "library_catalog.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = 1001
        with open(self.library_catalog) as b:
            content = b.readlines()
        for line in content:
            self.books_dict.update({str(id):{'book_title':line.replace("\n",""),'lender_name':'','lend_date':'', 'status':'Available'}})
            id += 1

    def display_books(self):
        print("------------------------------------------------ Library Catalog ------------------------------------------------")
        print("Book ID","\t", "Title")
        print("-----------------------------------------------------------------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key,"\t\t", value.get("book_title"), "- [", value.get("status"),"]")

    def issue_book(self):
        book_id = input("Enter Books ID : ")
        current_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        if not book_id.isdigit():
                print("***!!! Invalid input. Please enter a numeric Book ID. !!!***")
                return self.issue_book()
        if book_id in self.books_dict.keys():
            if not self.books_dict[book_id]['status'] == 'Available':
                print(f"!!! This book has already been borrowed by {self.books_dict[book_id]['lender_name']} on {self.books_dict[book_id]['lend_date']}. !!!")
                return self.issue_book()
            elif self.books_dict[book_id]['status'] == 'Available':
                your_name = input("Enter Your Name : ")
                self.books_dict[book_id]['lender_name'] = your_name
                self.books_dict[book_id]['lend_date'] = current_date
                self.books_dict[book_id]['status']= 'Already Issued'
                print("!!! Book Issued Successfully !!!\n")
        else:
            print("***!!! Book ID Not Found !!!***")
            return self.issue_book()

    def add_book(self):
        new_book = input("Enter Book Title : ")
        if new_book == "":
            return self.add_book()
        elif len(new_book) > 100:
            print("!!! The length of the book title exceeds the allowable limit of 100 characters. Please adhere to the specified title length constraint. !!!")
            return self.add_book()
        else:
            with open(self.library_catalog, "a") as b:
                b.writelines(f"{new_book}\n")
            self.books_dict.update({str(int(max(self.books_dict))+1):{'book_title':new_book,'lender_name':'','lend_date':'', 'status':'Available'}})
            print(f"!!! The addition of the book '{new_book}' was completed successfully. !!!")

    def return_book(self):
        book_id = input("Enter Books ID : ")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]['status'] == 'Available':
                print("!!! This book is currently accessible within the library. Kindly verify the book ID for confirmation. !!! ")
                return self.return_book()
            elif not self.books_dict[book_id]['status'] == 'Available':
                self.books_dict[book_id]['lender_name'] = ''
                self.books_dict[book_id]['lend_date'] = ''
                self.books_dict[book_id]['status']= 'Available'
                print("!!! Successfully Returned !!!\n")
        else:
            print("***!!! Book ID Not Found !!!***")



# Create a distinctive catalog of library items, ensuring careful and precise integration of this segment into the code for the successful implementation of the code.



if __name__ == "__main__":
    try:
        mylms = LMS("library_catalog.txt", "Dome of Athena")
        press_cmd_list = {"Display": "Display Books", "Issue": "Issue Book", "Add": "Add Book", "Return": "Return Book", "Quit": "Quit"}

        cmd_press = False
        while not (cmd_press == "q"):
            print(f"\n----------------------------- Welcome To {mylms.library_name}'s Library Management System -----------------------------\n")
            for key, value in press_cmd_list.items():
                print("Type", key, "To", value)
            cmd_press = input("\nType Command : ").lower()
            if cmd_press == "issue":
                print("\nCurrent Selection : ISSUE BOOK\n")
                mylms.issue_book()

            elif cmd_press == "add":
                print("\nCurrent Selection : ADD BOOK\n")
                mylms.add_book()

            elif cmd_press == "display":
                print("\nCurrent Selection : DISPLAY BOOKS\n")
                mylms.display_books()

            elif cmd_press == "return":
                print("\nCurrent Selection : RETURN BOOK\n")
                mylms.return_book()
            elif cmd_press == "quit":
                break
            else:
                continue
    except Exception as e:
        print("!!! Something went wrong. Please check. !!!")