


### **Exercise 2: Library System (Simplified)**
```python
# Library → Book? (Library has books)
# Book → Library? (Book knows where it is)
# Member → Book? (Member borrows books)
# Book → Member? (Book knows who borrowed it)

# Python implementation questions:
# 1. When Book is borrowed, which object updates the status?
# 2. How does Library know which Books are available?
# 3. What method does Member call to borrow a Book?
```

### **Exercise 3: Social Media (Basic)**

# User → Post? (User creates posts)
# Post → User? (Post knows its author)
# User → User? (User has friends)

# Python questions:

# 1. When creating a Post, does User add it to their posts list?
# 2. Does Post add itself to User's posts?
# 3. Who manages the friend relationship?


---

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


```

---
