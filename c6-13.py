#aggregation
#library
#print library name and all of its book

class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
    
    def add_book(self,book):
        self.books.append(book)
    
    def list_book(self):
        return [f"{book.name} by {book.author}" for book in self.books]

class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author
    
library=Library("New York Public Library")
book1= Book("Harry Potter"," JK Rowling")
book2 = Book("The Lord of the Rings", "J.R.R. Tolkien")
book3 = Book("The Hobbit", "J.R.R. Tolkien")
book4 = Book("1984", "George Orwell")
book5 = Book("Animal Farm", "George Orwell")
book6 = Book("Pride and Prejudice", "Jane Austen")
book7 = Book("To Kill a Mockingbird", "Harper Lee")
book8 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book9 = Book("The Catcher in the Rye", "J.D. Salinger")
book10 = Book("The Alchemist", "Paulo Coelho")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)
library.add_book(book7)
library.add_book(book8)
library.add_book(book9)
library.add_book(book10)

print(library.name)
print("**********")


for book in library.list_book():
    print(book)
    print("**********")
