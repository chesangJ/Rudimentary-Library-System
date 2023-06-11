
"""A python program to add a book to a library by name and author  and be able
 to view the details of the book
  """
def menu():
    print("[1] Add a book")
    print("[2] View Book Details")
    print("[0] Exit the program.")
"""Created a Library to hold books and allow the user to add a book and view details
of the book"""
class Library:
    def __init__(self):
        self.books={}#This is an empty dictionary to hold the books 
    
    def  add_book(self):
         """This function enables the user to add books by the book name and author """
         book = input("Enter books name: ")
         author = input("Enter authors name: ")

         self.books[book]=author #creates a new key-key value pair in the books dictionary

         print("Book added successfully")
    
    def show(self):
        """This function allows the user to view the details of the book that they have added"""
        if self.books:
            for book, author in self.books.items():
                print(f"Book: {book} | Author: {author}")
        else:
            print("No books in the library.")

library=Library()


#Calling the function
menu()
#Code to get the user input option
option=int(input("Enter your option: "))


while option!=0:
    if option==1:
        #method for adding a book to the library
        library.add_book()
    elif option==2:
        #method for viewing Book Details
         library.show()
    else:
        print("Invalid option")

    #Calling the menu funtion
    menu()
    #Code to get the user input option
    option=int(input("Enter your option: "))
