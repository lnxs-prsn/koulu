
## **Back to Battleship-Level Examples:**

Let me give you exercises at the **RIGHT level** for your Python course:

### **Exercise 1: Simple Game Objects**
```python
# Game → Player? (Game manages players)
# Player → Game? (Player knows which game they're in)
# Player → Card? (Player holds cards)
# Card → Player? (Card knows who holds it?)

# Python implementation level questions:
# 1. Should Game create Player objects, or are they created separately?
# 2. When Player plays a Card, who updates the game state?
# 3. If Player quits, what happens to their Cards?
```

### **Exercise 2: Library System (Simplified)**
```python
# Library → Book? (Library has books)
# Book → Library? (Book knows where it is)
# Member → Book? (Member borrows books)
# Book → Member? (Book knows who borrowed it)

# Python implementation questions:
# 1. When Book is borrowed, which object updates the status?
    -   library updates
# 2. How does Library know which Books are available?
    -   library checks its list of books and checks their state
# 3. What method does Member call to borrow a Book?
    -   I dont now exact but member calls the library and library calls method of the book
```

### **Exercise 3: Social Media (Basic)**
```python
# User → Post? (User creates posts)
# Post → User? (Post knows its author)
# User → User? (User has friends)

# Python questions:
# 1. When creating a Post, does User add it to their posts list?
# 2. Does Post add itself to User's posts?
# 3. Who manages the friend relationship?
```

---

## **The Battleship Lesson Applied:**

Remember your Battleship confusion? Let's break down what you **actually needed**:

### **What CONFUSED you in Battleship:**
```python
class Sea:
    def place_ship(self, ship, position):
        # Who calls this? Game? Player? Ship?
        pass

class Ship:
    def __init__(self, length):
        self.parts = []  # List of ShipPart objects
        # Does Ship create its own ShipParts?
        # Or does Sea create them when placing?

class ShipPart:
    def __init__(self, ship, position):
        # Does ShipPart know its Ship?
        # Does it know its position in Sea?
        pass

# The confusion: WHO STARTS THE ACTION?
# Option A: Game → Sea → creates Ship → creates ShipParts
# Option B: Player → creates Ship → asks Sea to place it
# Option C: Sea → creates grid of Squares → Ships occupy them
```

### **What You NEEDED to Understand:**
Not "system design" but **"method calling sequence"**:
1. `main()` creates `Game`
2. `Game` creates `Sea` and `Player`
3. `Player` calls `sea.place_ship(ship, position)`
4. `Sea` creates `Square` objects
5. `Ship` creates `ShipPart` objects
6. `Sea` associates `ShipPart` with `Square`

**That's it!** No legal frameworks, no conditional authority - just **which object creates/calls which**.

---



---

## **New, Scope-Appropriate Exercises:**

### **Exercise A: Coffee Shop**
```python
# Customer → Order? 
# Order → Barista?
# Barista → CoffeeMachine?
# CoffeeMachine → Coffee?

# Task: Write the METHOD CALLING SEQUENCE for:
# 1. Customer places order
# 2. Barista makes coffee
# 3. Customer receives coffee

# Focus: Which object's method calls which other object's method?
```

### **Exercise B: Online Quiz**
```python
# Quiz → Question?
# Question → Answer?
# User → QuizAttempt?
# QuizAttempt → QuestionResponse?

# Task: When user takes quiz:
# 1. Who creates the QuizAttempt?
# 2. Who stores each answer?
# 3. Who calculates the score?
```

### **Exercise C: Simple Bank (Back to Basics)**
```python
# Bank → Account? 
# Customer → Account?
# Account → Transaction?

# Task: For a withdrawal:
# 1. Does Customer call Bank or Account?
# 2. Who creates the Transaction record?
# 3. Who updates the balance?
```

---
