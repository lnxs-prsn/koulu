Hotel Room Booking
Purpose: Manage room reservations and guest stays.
Classes:

Room (room_number, room_type, price_per_night, amenities)

Guest (id, name, contact_info)

Booking (guest, room, check_in, check_out, total_charge)

Hotel (rooms, bookings, check_in_guest(), check_out_guest())

Core Challenge: Handle overlapping bookings, calculate stays spanning multiple nights, and manage room availability.

# **Python OOP Design Thinking Template** (No Code)

## **PROJECT ANALYSIS FRAMEWORK**

### **PART 1: UNDERSTAND THE PROBLEM**

What REAL-WORLD thing/process am I modeling?
booking a room in a hotel

What's the SIMPLEST possible version that would work?
room that has a number, type, price, amenities

What should users be able to DO?

1. :become a guest
2. :have a room to book
3. :checkin and check out

-

### **PART 2: IDENTIFY CORE COMPONENTS**

What are the main "things" involved?
• room (most important)
• guest
• booking
• hotel


For EACH room:

- What DATA does it need? room_number, room_type, price_per_night, amenities
- What ACTIONS can it do? ________________
- How does it relate to others? its independent but others booking and hotel rely on it

For EACH room:
- What DATA does it need? id, name, contact_info
- What ACTIONS can it do? 
- How does it relate to others? its independent but booking rely on it

For EACH room:
- What DATA does it need? guest, room, check_in, check_out, total_charge
- What ACTIONS can it do? calculate_total_charge(), validate checkin and checkout times are valid
- How does it relate to others? it relies on guest and room and hotel relies on it

For EACH room:
- What DATA does it need? rooms, bookings, 
- What ACTIONS can it do? check_in_guest(), check_out_guest()
- How does it relate to others? it relies on all the previous ones 

-

### **PART 3: DESIGN DECISIONS**

Structure:
[ ] Classes with composition (Container→Contained)

Communication:
[ ] Direct calls between objects

Data Storage:
[ ] In-memory only

-

PART 4: IMPLEMENTATION PLAN (Dependency-Driven Version)

STEP 1: Identify FOUNDATION from "Simplest Version"
From PART 1 Question 2: What's the SIMPLEST possible version that would work?

Answer: room that has a number, type, price, amenities

Therefore Phase 1 must build: room

STEP 2: Map DEPENDENCIES from Core Components
From PART 2: What depends on what?

room depends on nothing

guest depends on nothing

booking depends on room and guest
hotel  depends on booking and through it depends on room and guest


Therefore build order: 1 → 2 → 3

STEP 3: Determine COMMUNICATION PATTERN
From PART 3: How will objects talk?

Direct calls = Objects interact immediately



Therefore connection method: direct calls 

STEP 4: Address CORE CHALLENGE
From Problem Statement: What's the hardest part?

Challenge: Handle overlapping bookings, calculate stays spanning multiple nights, and manage room availability.

Therefore final phase must handle: validate that bookings dont over lap, calculate stays spanning multiple nights and manage room availability

STEP 5: Create PHASES Based on Dependencies
PHASE 1: Build room and guest
(Test: Can room store its data and can guest store its data ? ← Tests foundation)

PHASE 2: Add booking
(Connects via: direct communication Step 3 pattern)

PHASE 3: Add hotel
(Completes: validate that bookings dont over lap, calculate stays spanning multiple nights and manage room availability ← Solves Step 4 challenge)

STEP 6: Define STOP CRITERIA
From User Requirements in PART 1: What should users be able to DO?

1. :become a guest
2. :have a room to book
3. :checkin and check out
4. : do above without problems
   1. mainly validation before action


consider fro the step 6 this kind of organizing
easier to pass onward the task to someone else?
Core operations (create, deposit, withdraw)

✓ Validation (no overdraft, immutable transactions)

✓ Reporting (access statement)

### **PART 4: IMPLEMENTATION PLAN**
PHASE 1: Build room and guest
(Test: Can room store its data and can guest store its data ? ← Tests foundation)

PHASE 2: Add booking
(Connects via: direct communication Step 3 pattern)

PHASE 3: Add hotel
(Completes: validate that bookings dont over lap, calculate stays spanning multiple nights and manage room availability ← Solves Step 4 challenge)

STEP 6: Define STOP CRITERIA
From User Requirements in PART 1: What should users be able to DO?

1. :become a guest
2. :have a room to book
3. :checkin and check out
4. : do above without problems
   1. mainly validation before action
-

## **HOW TO USE THIS TEMPLATE:**

1. **Fill in Part 1** with YOUR project specifics
2. **Fill in Part 2** with YOUR objects/concepts  
3. **Make choices in Part 3** for YOUR design
4. **Create a plan in Part 4** for YOUR implementation
5. **THEN** write code based on YOUR answers
