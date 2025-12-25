### 1. **Library Book Tracker**

**Purpose**: Manage books, members, and checkouts.  
**Classes**:

- `Book` (title, author, ISBN, is_available)
- `Member` (name, member_id, borrowed_books)
- `Library` (holds collections of books and members; methods to check out/return books)

**Core Challenge**: Enforce borrowing rules (e.g., max 3 books per member, prevent duplicate checkouts).

-
-

# **Python OOP Design Thinking Template** (No Code)

## **PROJECT ANALYSIS FRAMEWORK**

### **PART 1: UNDERSTAND THE PROBLEM**

What REAL-WORLD thing/process am I modeling?
I am real world library system which has books,members, transaction
system would coordinate transactions of members borrowing books and members returning books,
library receiving new books library losing of books
library getting new members, library losing members
system would limit excessive borrowing by the members
system would limit borrowing same book by 2 members at the same time
____________________________________________

What's the SIMPLEST possible version that would work?
books that exist and can be borrowed and returned
members that exits and can borrow and return a book
  - member can only borrow available books
  - member cannot exceed borrow limit (3)
  - same book cannot be borrowed by more than 1 member at a time
  - when book is checked out it becomes unavailable when returned it becomes available

____________________________________________

What should users be able to DO?

1. :Book management
   1. create new book
   2. remove book
   3. check if book is available or checkedout
2. : Member management
   1. create new member
   2. delete member
   3. request a book borrowing
   4. request a return of book
   5. check which book are borrowed by member
3. :Library management
   1. checkout only available books and checkin books member is returning 
   2. tell new book to come to existence tell existing book to cease to exist
   3. tell new member to come to existence remove existing member
   4. uphold rules no duplicate checkouts, no more than 3 books in posession of member at a time

-

### **PART 2: IDENTIFY CORE COMPONENTS**

What are the main "things" involved?
• Library (most important)
• Book
• Member

For EACH thing:

- What DATA does it need? ________________
- What ACTIONS can it do? ________________
- How does it relate to others? __________

-

### **PART 3: DESIGN DECISIONS**

Structure:
[ ] Single class
[ ] Multiple independent classes  
[ ] Classes with inheritance (Parent→Child)
[ ] Classes with composition (Container→Contained)

Communication:
[ ] Direct calls between objects
[ ] Through central coordinator
[ ] Events/messages

Data Storage:
[ ] In-memory only
[ ] Files
[ ] Database (later)

-

### **PART 4: IMPLEMENTATION PLAN**

PHASE 1: Build ________________________
         (Test: Can it ________________?)

PHASE 2: Add _________________________
         (Connects via: _______________)

PHASE 3: Add _________________________
         (Completes: __________________)

STOP CRITERIA: _______________________

-

## **HOW TO USE THIS TEMPLATE:**

1. **Fill in Part 1** with YOUR project specifics
2. **Fill in Part 2** with YOUR objects/concepts  
3. **Make choices in Part 3** for YOUR design
4. **Create a plan in Part 4** for YOUR implementation
5. **THEN** write code based on YOUR answers
