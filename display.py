# display.py
from data import books, issued_books

def show_all_books():
    print("\n{:<10} {:<25} {:<20} {:<10}".format("ID", "Title", "Author", "Status"))
    
    if len(books) == 0:
        print("No books in library.")
    else:
        for b in books:
            print("{:<10} {:<25} {:<20} {:<10}".format(b["id"], b["title"], b["author"], b["status"]))

def show_issued_books():
    print(" Currently Issued Books ")
    if len(issued_books) == 0:
        print("No books issued.")
    else:
        for mid, bid in issued_books.items():
            for b in books:
                if b["id"] == bid:
                    print(f"Member {mid}  →  {b['title']} by {b['author']}")
                    break