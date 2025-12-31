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
- What ACTIONS can it do? add_balance(), take_from_balance(), update_transaction_record()
- How does it relate to others? not sure
 
For EACH transaction:

- What DATA does it need? amount, timestamp, type
- What ACTIONS can it do? nothing
- How does it relate to others? its acted on by the account
 
For EACH bank:

- What DATA does it need? list or dictionary of accounts that has list that takes tuples, 
- What ACTIONS can it do? create_account(), create transaction, transfer(between accounts), statement()
- How does it relate to others? could coordinate
 
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
