7. Restaurant Table Reservation
Purpose: Handle table bookings and orders.
Classes:

Table (table_number, capacity, is_reserved)

Reservation (customer_name, table, time, party_size)

MenuItem (name, price, category)

Order (table, items, total, status)

Restaurant (tables, menu, reservations)

Core Challenge: Enforce capacity limits, prevent overlapping reservations, and link orders to specific tables.



# **Python OOP Design Thinking Template** (No Code)

## **PROJECT ANALYSIS FRAMEWORK**

### **PART 1: UNDERSTAND THE PROBLEM**

What REAL-WORLD thing/process am I modeling?
restaurant table reservation and food ordering

What's the SIMPLEST possible version that would work?
tables that can be reserved, foods that can be ordered
restaurant that can be accessed

What should users be able to DO?

1. :reserve an table
2. :order food
3. :have an restaurant

-

### **PART 2: IDENTIFY CORE COMPONENTS**

What are the main "things" involved?
• table (most important)
• reservation
• menuitem
• order
• restaurant

For EACH table:

- What DATA does it need? table_number, capacity, is_reserved
- What ACTIONS can it do? reserve(), 
- How does it relate to others? instance is stored in the reservation and in the restaurant

For EACH reservation:

- What DATA does it need? customer_name, table, time, party_size
- What ACTIONS can it do? reserve_table()
- How does it relate to others? it stores an table instance and it is stored in the restaurant

For EACH menuitem:

- What DATA does it need? name, price, category
- What ACTIONS can it do? change_price
- How does it relate to others? its stored in the order and in the restaurant

For EACH order:

- What DATA does it need? table, items, total, status
- What ACTIONS can it do? calculate_total, add_items, toggle_status
- How does it relate to others? it stores menuitems, its stored in the restaurant

For EACH restaurant:

- What DATA does it need? tables, menu, reservations
- What ACTIONS can it do? store_tables, store_menu, store_reservations
- How does it relate to others? it stores the objects in the system
-

### **PART 3: DESIGN DECISIONS**

Structure:
[ ] Classes with composition (Container→Contained)

Communication:
[ ] Direct calls between objects and coordination through central object

Data Storage:
[ ] In-memory only

-

PART 4: IMPLEMENTATION PLAN (Dependency-Driven Version)

STEP 1: Identify FOUNDATION from "Simplest Version"
From PART 1 Question 2: What's the SIMPLEST possible version that would work?

Answer: tables that can be reserved, foods that can be ordered
restaurant that can be accessed

Therefore Phase 1 must build: tables

STEP 2: Map DEPENDENCIES from Core Components
From PART 2: What depends on what?

reservation depends on tables

order depends on menuitem

restaurant depends on all the objects directly or indirectly

independent objects are table and menuitem

Therefore build order: 1 → 2 → 3

STEP 3: Determine COMMUNICATION PATTERN
From PART 3: How will objects talk?

Direct calls = Objects interact immediately



Therefore connection method: direct communication

STEP 4: Address CORE CHALLENGE
From Problem Statement: What's the hardest part?

Challenge: enforce capacity limit, dont allow overlaps, link orders and tables

Therefore final phase must handle: data flow




consider fro the step 6 this kind of organizing
easier to pass onward the task to someone else?
Core operations (create, deposit, withdraw)

✓ Validation (no overdraft, immutable transactions)

✓ Reporting (access statement)

### **PART 4: IMPLEMENTATION PLAN**

PHASE 1: Build table
         (Test: Can it store its data?)
         build menuitem

PHASE 2: Add reservation 
         (Connects via: main())
        add order

PHASE 3: Add restaurant
         (Completes: stores)

STOP CRITERIA: 
-   enforce capacity limit, 
-   dont allow overlaps, 
-   link orders and tables

-

## **HOW TO USE THIS TEMPLATE:**

1. **Fill in Part 1** with YOUR project specifics
2. **Fill in Part 2** with YOUR objects/concepts  
3. **Make choices in Part 3** for YOUR design
4. **Create a plan in Part 4** for YOUR implementation
5. **THEN** write code based on YOUR answers
