# utils.py
from data import books

def search_book():
    sid = input("\nEnter Book ID to search: ")
    found = False
    for b in books:
        if b["id"] == sid:
            print(f"Found: {b['title']} by {b['author']} | Status: {b['status']}")
            found = True
    if not found:
        print("Book not found!")

def delete_book():
    did = input("\nEnter Book ID to delete: ")
    for b in books:
        if b["id"] == did:
            books.remove(b)
            print("Book deleted successfully!")
            return
    print("Book not found!")