DOMAIN MODEL: Library Book Tracker
CORE DOMAIN
A system that manages the inventory of books and regulates their lending to registered members. The core challenge is enforcing business rules to ensure the integrity of the library's collection and the fairness of its lending policy, specifically limiting simultaneous borrows and preventing duplicate checkouts.

KEY CONCEPTS
Concept	Definition	Type (Entity/VO/Service)
Book	A physical or digital item that can be borrowed. Defined by its title, author, and a unique identifier.	Entity
ISBN	International Standard Book Number. A unique, immutable identifier for a book edition.	Value Object
Member	A registered person authorized to borrow books from the library.	Entity
Library	The central coordinating entity that manages the collection of books and members, and orchestrates checkout/return transactions.	Entity / Aggregate Root
Checkout	The act of a Member borrowing a Book for a period of time. A record of this transaction.	Entity (likely within an Aggregate)
BorrowedBooks	A collection of books currently checked out by a Member. It is critical for rule enforcement.	Value Object / Concept within Member
AGGREGATES
Library Aggregate
Root: Library
Purpose: Protects the core business rules governing the lending of books, ensuring the system's invariants are never violated.
Rules:

A Member cannot have more than 3 books checked out simultaneously.

A specific physical Book copy cannot be checked out if it is already checked out (no duplicate active checkouts for the same book instance).

USE CASES
UC1: Check Out a Book
Actor: Librarian or Member (via self-service)
Steps:

System identifies the Member and their current BorrowedBooks count/list.

System validates the Book is available (is_available == true).

Enforce Rule: System ensures Member has fewer than 3 books borrowed.

Enforce Rule: System ensures this specific Book copy is not already checked out (redundant but critical check).

System creates a Checkout record, updates the Book status to unavailable, and adds the book to the Member's borrowed_books.

System confirms successful checkout to the actor.

UC2: Return a Book
Actor: Librarian or Member
Steps:

System identifies the Book being returned.

System locates the active Checkout record for this Book.

System updates the Book status to available and removes it from the Member's borrowed_books.

System archives or marks the Checkout record as completed.

System confirms successful return.

GLOSSARY
Checkout: The transaction where a Member takes possession of a Book for a limited time.

Available: The state of a Book where it is physically present in the library and not currently assigned to an active Checkout.

BorrowedBooks: The list of books a Member currently has checked out. Its count is central to the "max 3 books" rule.