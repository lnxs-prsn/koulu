4. E-Commerce Product & Order System
Purpose: Manage products, shopping carts, and orders.
Classes:

Product (id, name, price, stock_quantity)

Customer (id, name, email, address)

Cart (customer, items, total_price)

Order (order_id, customer, items, status: 'pending'/'shipped'/'delivered')

!!!Core Challenge: Ensure stock updates when items are purchased, prevent negative inventory, and manage order state transitions.



# **Python OOP Design Thinking Template** (No Code)

## **PROJECT ANALYSIS FRAMEWORK**

### **PART 1: UNDERSTAND THE PROBLEM**

What REAL-WORLD thing/process am I modeling?
process is modeling to going to shop and buying a product from the shop

What's the SIMPLEST possible version that would work?
customer takes product puts it in to cart and pays for the product then product stock is reduced.

What should users be able to DO?

1. :create user account, browse to see if products are available or not
2. :put/remove products to/from cart (cannot put non available product to cart)
3. :pay for the product (order) and get a receipt update the stock

-

### **PART 2: IDENTIFY CORE COMPONENTS**

What are the main "things" involved?
• product (most important)
• customer
• order
• cart




For EACH product:

- What DATA does it need? id, name, price, stock_quantity
- What ACTIONS can it do? update_stock(), check_availability(), 
- How does it relate to others? customer tells cart adds it to cart, order tells it to update its stock_quantity

For EACH customer:

- What DATA does it need? id, name, email, address
- What ACTIONS can it do? place_order(),tell cart to add product to cart
- How does it relate to others? tells cart to add product to itself, tells cart to checkout

For EACH order:

- What DATA does it need? order_id, customer object, items product objects, status: 'pending'/'shipped'/'delivered'
- What ACTIONS can it do? update_stock(), update_status(), place_order() 
- How does it relate to others? it sends products to customer, it tells product to update its amount

For EACH cart:

- What DATA does it need? customer object, items multiple product objects, total_price
- What ACTIONS can it do? calculate_total(items), add_item(product, quantity), remove_item(product), clear(), checkout()
- How does it relate to others? it stores product objects


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