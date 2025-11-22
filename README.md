# Library Management System

A simple, console-based library management system built in Python with **in-memory storage** - no database, no file handling.

## Overview

This project implements a menu-driven library system in which a librarian will be able to add, view, search, and delete books, plus issue and return them. All data is temporarily stored during runtime in lists and dictionaries and will be cleared when the program exits.
## Features
- Add new books
- View all books in a formatted table
- Search book by Book ID
- Delete book permanently
- Issue book to a member/student
- Return issued book
- View currently issued books
- 6 well-structured modules for clean code organization

- Professional console output with proper alignment
- Zero external dependencies

## Technologies Used

- **Language**: Python 3.x



- **Data Storage**: In-memory (lists & dictionaries)

- **No external libraries required**

## Project Structure

---
LibraryProject/
├── main.py      → Program entry & menu
├── book.py      → Add new book
├── member.py    → Issue & return logic
├── utils.py     → Search & delete operations
├── display.py   → Formatted output functions
├── data.py      → Central in-memory storage
└── README.md    → This file

## How to Run
1. Clone or download this repository
2. Open terminal in the project folder
3. Run:
   ```bash
   python main.py
4. Use options 1–8 from the menu

Note: All data is lost on exit (by design).

## Testing Instructions

1. Add a few books → Option 1
2. Issue a book → Option 5
3. Try issuing the same book again → Should be blocked
4. Return the book → Option 6
5. Check issued list → Option 7
6. Delete a book and verify it’s gone → Option 4

## Screenshots
(Saved in screenshots file and also there in project report)

1. Main menu
2. Adding a book
3. Viewing all books
4. Successful issue & return
5. Issued books report

**Developed by**: Manishika
**Language**: Python
**Last Updated**: November 2025