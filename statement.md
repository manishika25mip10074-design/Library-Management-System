 `statement.md`

ClassCastException
# Project Statement — Library Management System
Problem Statement

Design a lightweight, console-based library management system in Python. The system should support full lifecycle of a book and transaction tracking using only in-memory data structures. No files, databases, or exception handling are allowed.
## Scope
The system provides full functionality to manage a small library during a single session. It focuses on clean architecture, modularity, and user-friendly interaction while deliberately avoiding the use of persistent storage.

## Target Users
- Librarians managing small collections
- Students learning about Python modular programming

- Developers looking for a clean, educational console application
High-Level Features

1. **Book Management**
- Add, search, view, and delete books
- Enforces Unique Book ID via user input
2. **Transaction Management
- Issue the books to members (status: Issued)

- Return books (status: Available)
- Prevents double issuance 
3. **Reporting** - Display full inventory in a tabular format - Real time issued books with member mapping 
4. **Architecture Highlights** - 6 independent modules with single responsibility Centralized data storage in `data.py` - Clear separation of concerns - Formatted, readable console interface - Pure Python — no external dependencies 
**Developed by**: [Manishika] **Language**: Python 3 **Storage**: In-memory only