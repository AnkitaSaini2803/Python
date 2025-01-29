''' 19/1/2025
Write a Library class with no_of_books and books as two instance variables. 
Write a program to create a library from this Library class and show how you can
print all books, add a book and get the number of books using different methods.
Show that your program doesnt persist the books after the program is stopped!
'''
# class Library:
#     def __init__(self):
#         self.no_of_books=0
#         self.books=[]

#     def add_books(self):
#        for i in range(5):
#         name=input(f"Enter Name of book {i+1} :")
#         # print(self.name)
#         self.books.append(name)
#         self.no_of_books+=1
#         print(self.books)

#     def print_books(self):
#        print(f"The libary has {self.no_of_books} books")
      
# obj=Library()
# obj.add_books()  
# obj.print_books()
'''List of books is empty
No of books is also zero
'''

class Books_Hall:
    def __init__(self):
        self.books=[]
        self.no_of_books=0

    def add_books(self):
        for i in range(4):
         name=input(f"Enter the name of book {i+1} : ")
         self.books.append(name)
         self.no_of_books+=1
         print(self.books)

    def display_books(self):
        print(f"You have Total {self.no_of_books} books in your Library")
      
        print(f"The name of books that are present in your library are:")
        for j in self.books:
          print(f"{j}")

obj=Books_Hall()
obj.add_books()
obj.display_books()