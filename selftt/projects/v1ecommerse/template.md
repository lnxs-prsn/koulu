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
- What ACTIONS can it do? add_stock(),decrease_stock(), check_availability(), 
- How does it relate to others? Contained in Cart items, referenced in Order items

For EACH customer:

- What DATA does it need? id, name, email, address
- What ACTIONS can it do? Create account, browse products, manage cart, place orders
- How does it relate to others? owns cart, places order

For EACH cart:

- What DATA does it need? customer (reference), items (list of products with quantities), total_price
- What ACTIONS can it do? Add/remove items, calculate total, clear cart, convert to order
- How does it relate to others? Belongs to one Customer, becomes an Order upon checkout



For EACH order:

- What DATA does it need? order_id, customer, items, status ('pending'/'shipped'/'delivered')
- What ACTIONS can it do? Place order (updates product stock), update status, cancel order (potentially restock items)
- How does it relate to others? Created from Cart, references Customer and 
-

### **PART 3: DESIGN DECISIONS**

Structure:

[x] Classes with composition (Container→Contained)

Communication:
[x] Direct calls between objects


Data Storage:
[x] In-memory only

-



PART 4: IMPLEMENTATION PLAN (Dependency-Driven Version)

STEP 1: Identify FOUNDATION from "Simplest Version"
From PART 1 Question 2: What's the SIMPLEST possible version that would work?

Answer: customer takes product puts it in to cart and pays for the product then product stock is reduced.

Therefore Phase 1 must build: customer

STEP 2: Map DEPENDENCIES from Core Components
From PART 2: What depends on what?

cart depends on customer

order depends on cart

product depends on customer/order

Therefore build order: 1 → 2 → 3

STEP 3: Determine COMMUNICATION PATTERN
From PART 3: How will objects talk?

Direct calls = Objects interact immediately



Therefore connection method: composition

STEP 4: Address CORE CHALLENGE
From Problem Statement: What's the hardest part?

Challenge: Core Challenge: Ensure stock updates when items are purchased, prevent negative inventory, and manage order state transitions.

Therefore final phase must handle: validation and state update

STEP 5: Create PHASES Based on Dependencies
PHASE 1: Build product
(Test: Can it store data update stock amount? ← Tests foundation)

PHASE 2: Add customer
(Connects via: composition ← Uses Step 3 pattern)

PHASE 3: Add cart and order
(Completes: manages validation and state update ← Solves Step 4 challenge)

STEP 6: Define STOP CRITERIA
From User Requirements in PART 1: What should users be able to DO?

✅ have an account and have an cart 

✅ browse and add only products with available stock to cart and check out

✅ update state of available stock after checkout


consider fro the step 6 this kind of organizing
easier to pass onward the task to someone else?
Core operations (create, deposit, withdraw)

✓ Validation (no overdraft, immutable transactions)

✓ Reporting (access statement)




### **PART 4: IMPLEMENTATION PLAN**

PHASE 1: Build product
(Test: Can it store data update stock amount? ← Tests foundation)

PHASE 2: Add customer
(Connects via: composition ← Uses Step 3 pattern)


PHASE 3: Add cart and order
(Completes: manages validation and state update ← Solves Step 4 challenge)

STOP CRITERIA: 
✅ have an account and have an cart 

✅ browse and add only products with available stock to cart and check out

✅ update state of available stock after checkout
-

## **HOW TO USE THIS TEMPLATE:**

1. **Fill in Part 1** with YOUR project specifics
2. **Fill in Part 2** with YOUR objects/concepts  
3. **Make choices in Part 3** for YOUR design
4. **Create a plan in Part 4** for YOUR implementation
5. **THEN** write code based on YOUR answers