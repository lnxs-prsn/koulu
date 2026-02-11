Fitness Class Scheduler
Purpose: Schedule fitness classes and manage memberships.
Classes:

Member (id, name, membership_type)

Trainer (id, name, specialty)

FitnessClass (name, trainer, datetime, max_capacity)

Booking (member, fitness_class)

Gym (classes, members, trainers)

Core Challenge: Enforce class capacity, prevent double bookings, and check membership validity.



# **Python OOP Design Thinking Template** (No Code)

## **PROJECT ANALYSIS FRAMEWORK**

### **PART 1: UNDERSTAND THE PROBLEM**

What REAL-WORLD thing/process am I modeling?
its fitness class booking in the gym

What's the SIMPLEST possible version that would work?
member booking an fitness class that has an trainer

What should users be able to DO?

1. :create member, trainer, 
2. :have an trainer in fitnessclass and member booking an fitness class
3. : ensure that there is no over booking of classes. no double booking and only for members 

-

### **PART 2: IDENTIFY CORE COMPONENTS**

What are the main "things" involved?
• member (most important)
• trainer
• fitnessclass
• booking
• gym



For EACH member:

- What DATA does it need? id, name, membership_type
- What ACTIONS can it do? validate membership type
- How does it relate to others? instance is stored in booking and in gym

For EACH trainer:

- What DATA does it need? id, name, specialty
- What ACTIONS can it do? get_specialty
- How does it relate to others? instance is stored in fitnessclass and in gym

For EACH fitnessclass:

- What DATA does it need? name, trainer, datetime, max_capacity
- What ACTIONS can it do? get_max_capacity, get_date_time, set_date_time
- How does it relate to others? is stored in the booking and in gym

For EACH booking:

- What DATA does it need? member, fitness_class
- What ACTIONS can it do? book_fitness_class, get_list_of_bookings
- How does it relate to others? its not stored anywhere perhaps its stored in class attribute

For EACH gym:

- What DATA does it need? classes, members, trainers
- What ACTIONS can it do? validate_class_availability, 
- How does it relate to others? it stores instances of 3 classes and coordinates interaction of instances
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

Answer:  member booking an fitness class that has an trainer

Therefore Phase 1 must build: member

STEP 2: Map DEPENDENCIES from Core Components
From PART 2: What depends on what?

member depends on is independed

trainer depends on is independent

fitnessclass depends on trainer

booking depends on member and fitnessclass which in turn depends on trainer

gym depends on member, trainers, fitnessclass, should also store the bookings but for some reason project designer left it out


Therefore build order: 1 → 2 → 3
member, trainer, fitness class and booking
STEP 3: Determine COMMUNICATION PATTERN
From PART 3: How will objects talk?


Coordinator = Objects go through middleman


Therefore connection method: coordinator

STEP 4: Address CORE CHALLENGE
From Problem Statement: What's the hardest part?

Challenge: Core Challenge: Enforce class capacity, prevent double bookings, and check membership validity.

Therefore final phase must handle: ensuring capacity limits of class, prevent members booking twice and check members before booking them a class

STEP 5: Create PHASES Based on Dependencies
PHASE 1: Build member, trainer, fitness class, booking
(Test: Can they interact? ← Tests foundation)

PHASE 2: Add gym
(Connects via: coordination ← Uses Step 3 pattern)

PHASE 3: Add ensuring capacity limits of class, prevent members booking twice and check members before booking them a class
(Completes: the program ← Solves Step 4 challenge)

STEP 6: Define STOP CRITERIA
From User Requirements in PART 1: What should users be able to DO?
1. :create member, trainer, 
2. :have an trainer in fitnessclass and member booking an fitness class
3. : ensure that there is no over booking of classes. no double booking and only for members 



consider fro the step 6 this kind of organizing
easier to pass onward the task to someone else?
Core operations (create, deposit, withdraw)

✓ Validation (no overdraft, immutable transactions)

✓ Reporting (access statement)


### **PART 4: IMPLEMENTATION PLAN**

PHASE 1: Build member, trainer, fitness class, booking
(Test: Can they interact? ← Tests foundation)

PHASE 2: Add gym
(Connects via: coordination ← Uses Step 3 pattern)

PHASE 3: Add ensuring capacity limits of class, prevent members booking twice and check members before booking them a class
(Completes: the program ← Solves Step 4 challenge)

STOP CRITERIA: 
1. :create member, trainer, 
2. :have an trainer in fitnessclass and member booking an fitness class
3. : ensure that there is no over booking of classes. no double booking and only for members 

-

## **HOW TO USE THIS TEMPLATE:**

1. **Fill in Part 1** with YOUR project specifics
2. **Fill in Part 2** with YOUR objects/concepts  
3. **Make choices in Part 3** for YOUR design
4. **Create a plan in Part 4** for YOUR implementation
5. **THEN** write code based on YOUR answers


