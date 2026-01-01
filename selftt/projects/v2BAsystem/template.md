### 3. **Bank Account System**
**Purpose**: Handle basic banking operations with transaction records.  
**Classes**:
- `Account` (account_number, owner_name, balance, transactions)
- `Transaction` (amount, timestamp, type: 'deposit'/'withdrawal')
- `Bank` (manages multiple accounts; methods to create, transfer, statement)

**Core Challenge**: Prevent invalid operations (e.g., overdrafts), and ensure transaction immutability after creation.

# **Python OOP Design Thinking Template** (No Code)

## **PROJECT ANALYSIS FRAMEWORK**

### **PART 1: UNDERSTAND THE PROBLEM**

What REAL-WORLD thing/process am I modeling?
creating an bank account and making an transaction with the account

What's the SIMPLEST possible version that would work?
account with owner and balance
What should users be able to DO?

1. :create account, with an owner,  
2. :add to balance take from balance
3. :have an way to look back to see when something was taken or added to account

-

### **PART 2: IDENTIFY CORE COMPONENTS**

What are the main "things" involved?
• account (most important)
• transaction
• bank

For EACH account:

- What DATA does it need? id, owner, balance, transaction record: alist of tuples
- What ACTIONS can it do? deposit() withraw() # both these functions have the functionality to create transaction instance
- How does it relate to others? contains multiple transaction objects is managed by the bank object
 
For EACH transaction:

- What DATA does it need? amount, timestamp, type
- What ACTIONS can it do? get_details()(formatted info), is_valid()(positive amount, valid type)
- How does it relate to others? created by the account during deposit/witdrawal, once created immutable
 
For EACH bank:

- What DATA does it need? account(dict mapping account_id,-> account object)
- What ACTIONS can it do? create_account(account_number), find_account_by_owner_name(name) 
- How does it relate to others? contains and manages multiple account objects, coordinates transfer between accounts
 
### **PART 3: DESIGN DECISIONS**

Structure:
[ ] Classes with composition (Container→Contained)

Communication:
[ ] Through central coordinator

Data Storage:
[ ] In-memory only

-

### **PART 4: IMPLEMENTATION PLAN**

PHASE 1:  Build account
         (Test: Can it deposit/withdraw? )

PHASE 2: Add transaction, make it immutable class
         (Connects via: account creates it when doing deposit or withdrawal )

PHASE 3: Add bank
         (Completes: no invalid transactions and no mutable transaction objecst, coordinates transaction between objects and system level oversight )

STOP CRITERIA: 
  -   create account, deposit and withdrawal features
  -   account cannot over draft and transactions are immutable
  -   able to access statement
  -   

-

## **HOW TO USE THIS TEMPLATE:**

1. **Fill in Part 1** with YOUR project specifics
2. **Fill in Part 2** with YOUR objects/concepts  
3. **Make choices in Part 3** for YOUR design
4. **Create a plan in Part 4** for YOUR implementation
5. **THEN** write code based on YOUR answers
