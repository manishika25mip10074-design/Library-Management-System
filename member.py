# member.py
from data import books, issued_books

def issue_book():
    mid = input("\nEnter Member ID   : ")
    bid = input("Enter Book ID     : ")
    
    for b in books:
        if b["id"] == bid:
            if b["status"] == "Available":
                b["status"] = "Issued"
                issued_books[mid] = bid
                print(f"Book issued to {mid}")
            else:
                print("Book already issued!")
            return
    print("Book not found!")

def return_book():
    mid = input("\nEnter Member ID   : ")
    if mid in issued_books:
        bid = issued_books[mid]
        for b in books:
            if b["id"] == bid:
                b["status"] = "Available"
                print(f"Book returned by {mid}")
                del issued_books[mid]
                return
    else:
        print("No book issued to this member!")