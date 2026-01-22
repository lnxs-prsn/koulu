6. Vehicle Rental System
Purpose: Manage fleet of vehicles and rentals.
Classes:

Vehicle (id, model, daily_rate, is_available)

Customer (id, name, license_number)

Rental (vehicle, customer, start_date, end_date, total_cost)

Fleet (vehicles, available_vehicles(), rent_vehicle(), return_vehicle())

Core Challenge: Calculate rental costs based on days, prevent double rentals, and validate rental periods.
# **Python OOP Design Thinking Template** (No Code)
## **PROJECT ANALYSIS FRAMEWORK**
### **PART 1: UNDERSTAND THE PROBLEM**
What REAL-WORLD thing/process am I modeling?
vehicle rental system

What's the SIMPLEST possible version that would work?
vehicles that can be rented
customers that can rest
rental that has vehicles for rental

What should users be able to DO?

1. :create a vehicle
2. :create customer 
3. : rent a vehicle to customer
4. :fleet to store existing vehicles

-

### **PART 2: IDENTIFY CORE COMPONENTS**

What are the main "things" involved?
• vehicle (most important)
• customers
• rental
• fleet

For EACH vehicle:

- What DATA does it need? id, model, daily_rate, is_available
- What ACTIONS can it do? check availability
- How does it relate to others? stored in the fleet, interacted by the rental

For EACH customer:

- What DATA does it need? id, name, license_number
- What ACTIONS can it do? request_rent
- How does it relate to others? stores vehicle license number

For EACH rental:

- What DATA does it need? vehicle, customer, start_date, end_date, total_cost
- What ACTIONS can it do? 
- How does it relate to others? it stores vehicle and customer

For EACH fleet:

- What DATA does it need? vehicles, 
- What ACTIONS can it do? available_vehicles(), rent_vehicle(), return_vehicle()
- How does it relate to others? it coordinates vehicle, customer and rental

-

### **PART 3: DESIGN DECISIONS**

Structure:
[ ] Classes with composition (Container→Contained)

Communication:
[ ] Through central coordinator

Data Storage:
[ ] In-memory only

-

PART 4: IMPLEMENTATION PLAN (Dependency-Driven Version)

STEP 1: Identify FOUNDATION from "Simplest Version"
From PART 1 Question 2: What's the SIMPLEST possible version that would work?

Answer: vehicles that can be rented
customers that can rest
rental that has vehicles for rental


Therefore Phase 1 must build: vehicle

STEP 2: Map DEPENDENCIES from Core Components
From PART 2: What depends on what?

vehicle depends on ________________

customer depends on vehicle

rental depends on vehicle, customer

fleet depends on vehicle

Therefore build order: 1 → 2 → 3

STEP 3: Determine COMMUNICATION PATTERN
From PART 3: How will objects talk?


Coordinator = Objects go through middleman


Therefore connection method: coordinator

STEP 4: Address CORE CHALLENGE
From Problem Statement: What's the hardest part?

Challenge: validate rental dates, no double rentals

Therefore final phase must handle: validation

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

PHASE 1: Build vehicle
         (Test: Can it store vehicle data?)

PHASE 2: Add customer and rental
         (Connects via: flee )

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
