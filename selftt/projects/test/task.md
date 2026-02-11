PART B: OOP Design (15 min)
Same scenario: Library search feature.
Task: Fill your OOP template (Parts 1-4 only, skip implementation phases for now).
Part 1: Real-world thing? Simplest version? 3 user actions?
Part 2: Main "things" involved. For each: data needed, actions possible, relations to others?
Part 3: Structure choice? Communication pattern? Data storage?
Part 4: STOP CRITERIA only — what 3 things must work for this feature to be "done"?

# **Python OOP Design Thinking Template** (No Code)
search_interface keyword, methods seach()
book, title, author, available methods set_available, get_available
library books, users, methods, create_book, create_user, get_list_of_books, set_list_of_books, borrow, return
user name, address, borrowed books methods get borrowed books, set_borrowed_books 
## **PROJECT ANALYSIS FRAMEWORK**

### **PART 1: UNDERSTAND THE PROBLEM**

What REAL-WORLD thing/process am I modeling?
searching book in library

What's the SIMPLEST possible version that would work?
user that can search existing books of the librarys

What should users be able to DO?

1. :search the books of the librarys

-

### **PART 2: IDENTIFY CORE COMPONENTS**

What are the main "things" involved?
• searchInterface (most important)
• books
• user
• library


For EACH searchInteface:

- What DATA does it need? keyword
- What ACTIONS can it do? search
- How does it relate to others? it asks library if the keyword is found in the book list


For EACH books:

- What DATA does it need? title, author, available
- What ACTIONS can it do? set_available, get_available
- How does it relate to others? its stored in the library instance
For EACH user:

- What DATA does it need? name, address, borrewed_books
- What ACTIONS can it do? get_borrowed_books, set_borrowed_books
- How does it relate to others? its stored in the library but it also stores book instances

For EACH library:

- What DATA does it need? books, users
- What ACTIONS can it do?  create_book, create_user, get_list_of_books, set_list_of_books, borrow, return
- How does it relate to others? its the coordinator for most but it has direct communication with the search interface


### **PART 3: DESIGN DECISIONS**

Structure:
[ ] Classes with composition (Container→Contained)

Communication:
[ ] Direct calls between objects
[ ] Through central coordinator

Data Storage:
[ ] In-memory only

-


PART 4: IMPLEMENTATION PLAN (Dependency-Driven Version)

STEP 1: Identify FOUNDATION from "Simplest Version"
From PART 1 Question 2: What's the SIMPLEST possible version that would work?

Answer: _______________________

Therefore Phase 1 must build: _______________________

STEP 2: Map DEPENDENCIES from Core Components
From PART 2: What depends on what?

________________ depends on ________________

________________ depends on ________________

________________ depends on ________________

Therefore build order: 1 → 2 → 3

STEP 3: Determine COMMUNICATION PATTERN
From PART 3: How will objects talk?

Direct calls = Objects interact immediately

Coordinator = Objects go through middleman

Events = Objects broadcast/listen

Therefore connection method: ________________

STEP 4: Address CORE CHALLENGE
From Problem Statement: What's the hardest part?

Challenge: ________________

Therefore final phase must handle: ________________

STEP 5: Create PHASES Based on Dependencies
PHASE 1: Build ________________________
(Test: Can it ________________? ← Tests foundation)

PHASE 2: Add _________________________
(Connects via: _______________ ← Uses Step 3 pattern)

PHASE 3: Add _________________________
(Completes: __________________ ← Solves Step 4 challenge)

STEP 6: Define STOP CRITERIA
From User Requirements in PART 1: What should users be able to DO?

✅ ________________________

✅ ________________________

✅ ________________________


consider fro the step 6 this kind of organizing
easier to pass onward the task to someone else?
Core operations (create, deposit, withdraw)

✓ Validation (no overdraft, immutable transactions)

✓ Reporting (access statement)
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
