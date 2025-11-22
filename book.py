# book.py
from data import books

def add_book():
    print(" Add New Book ")
    bid = input("Enter Book ID     : ")
    title = input("Enter Book Title  : ")
    author = input("Enter Author Name : ")
    
    book = {"id": bid, "title": title, "author": author, "status": "Available"}
    books.append(book)
    print("Book added successfully!")