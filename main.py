# main.py
from book import add_book
from member import issue_book, return_book
from utils import search_book, delete_book
from display import show_all_books, show_issued_books

print("LIBRARY MANAGEMENT SYSTEM")
print("Data will be lost when you close the program!\n")

while True:
    
    print("        LIBRARY MANAGEMENT SYSTEM")
    
    print("1. Add New Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. View Issued Books")
    print("8. Exit")
    
    choice = input("\nEnter your choice (1-8): ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        show_all_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        issue_book()
    elif choice == "6":
        return_book()
    elif choice == "7":
        show_issued_books()
    elif choice == "8":
        print("\nThank You! Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")