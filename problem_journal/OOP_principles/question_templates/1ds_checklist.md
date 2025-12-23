# OOP PRINCIPLES CHECKLIST FOR STUDENT PROJECTS

**Use this after you've designed your classes, before you start coding:**

## 🎯 THE 5-STUDENT PRINCIPLES

### 1. **ONE JOB RULE**

```python

# ❌ BAD: Multiple jobs
class UserManager:
    def validate_email(self):...    # Job 1: Validation
    def save_to_database(self):...  # Job 2: Database
    def send_welcome_email(self):... # Job 3: Email

# ✅ GOOD: One job each
class EmailValidator: ...    # Only validates
class UserRepository: ...    # Only saves
class EmailService: ...      # Only sends emails
```

**Ask:** "Can I describe this class's job without using 'and' or 'or'?"

### 2. **MY STUFF, MY RULES**

```python

# ❌ BAD: Others control my data
class BankAccount:
    def __init__(self):
        self.balance = 0  # Public - anyone can change!

# ✅ GOOD: I control my data
class BankAccount:
    def __init__(self):
        self._balance = 0  # Private
    
    def deposit(self, amount):  # Controlled access
        if amount > 0:
            self._balance += amount
    
    def get_balance(self):
        return self._balance
```

**Ask:** "Are my class's important data marked with `_` (private)?"

### 3. **HAVE, DON'T BE**

```python
# ❌ BAD: "IS-A" inheritance chain
class Animal:
    def eat(self):...

class Bird(Animal):
    def fly(self):...

class Penguin(Bird):  # Penguins can't fly!
    def fly(self):
        raise Error("Can't fly!")  # Problem!

# ✅ GOOD: "HAS-A" composition
class Animal:
    def __init__(self, mover):
        self.mover = mover  # Has a mover
    
    def move(self):
        self.mover.move()

class Flyer:
    def move(self):
        print("Flying!")

class Swimmer:
    def move(self):
        print("Swimming!")

penguin = Animal(Swimmer())  # Penguin has swimming ability
```

**Ask:** "Am I using HAS-A (composition) more than IS-A (inheritance)?"

### 4. **TELL, DON'T BEG**

```python
# ❌ BAD: Asking for data, then doing work
def process_order(order):
    items = order.get_items()      # Ask for data
    total = calculate_total(items) # Do work myself
    order.set_total(total)         # Set data back

# ✅ GOOD: Tell object what to do
def process_order(order):
    order.calculate_total()  # Tell order to do it
```

**Ask:** "Am I telling objects what to do, or asking for their data to do it myself?"

### 5. **GET HELP, DON'T MAKE IT**

```python
# ❌ BAD: Creating dependencies inside
class OrderProcessor:
    def __init__(self):
        self.database = Database()  # Creates dependency
    
    def process(self, order):
        self.database.save(order)

# ✅ GOOD: Get help passed in
class OrderProcessor:
    def __init__(self, database):  # Receives dependency
        self.database = database
    
    def process(self, order):
        self.database.save(order)

# Usage:
db = Database()
processor = OrderProcessor(db)  # We give it the help
```

**Ask:** "Am I passing in helpers via `__init__`, or creating them inside?"

---

## 🚦 STUDENT-FRIENDLY RED FLAGS

**STOP if you see these in your design:**

### 🔴 **God Class Alert**

- Class has 8+ methods
- Class name contains "Manager", "Processor", "Handler"
- You can't describe its job in 5 words

### 🔴 **Data Dumping Ground**

- Class is just getters/setters (`get_x()`, `set_x()`)
- No real behavior, just holds data
- Other classes constantly ask it for data

### 🔴 **Inheritance Chain**

- More than 2 levels of inheritance (Grandparent → Parent → Child)
- Subclass overriding parent methods with `pass` or `raise NotImplementedError`
- Using inheritance just to reuse code

### 🔴 **Tight Coupling**

- Class mentions specific other class names everywhere
- Changing one class breaks many others
- Hard to test without running the whole system

---

## ✅ PRE-SUBMISSION CHECK (5 minutes)

Before handing in your assignment, ask:

1. **Job Check:** "What's this class's one job?" → Should be 5-word answer max
2. **Privacy Check:** Look for `_variable` names → Important data should be private
3. **Composition Check:** Count `self.thing = thing` vs `class Child(Parent)`
4. **Talk Check:** Are methods telling objects (`obj.do_thing()`) vs asking (`data = obj.get_data()`)?
5. **Test Check:** Can you create the class with fake helpers for testing?

---

## 🎓 TEACHER EXPECTATIONS BY LEVEL

### **Beginner (First OOP Project)**
✅ Expected: SRP, basic encapsulation  
✅ Good: Some composition, not just inheritance  
⚠️ OK: Some tight coupling, simple designs  
🎉 Celebration: Working objects that collaborate!

### **Intermediate (2-3 Projects Done)**
✅ Expected: All 5 student principles  
✅ Good: Dependency injection, tell-don't-ask  
⚠️ OK: Some advanced principle violations  
🎉 Celebration: Testable, flexible design!

### **Advanced (Final Projects)**
✅ Expected: SOLID principles awareness  
✅ Good: Design patterns where appropriate  
🎉 Celebration: Professional-level OOP design!

---

## 📝 QUICK REFERENCE CARD

```python
# GOOD STUDENT OOP TEMPLATE
class GoodStudentClass:
    """One clear job in this docstring"""
    
    def __init__(self, helper1, helper2):  # Get help
        self._my_data = None      # Private data
        self.helper1 = helper1    # Composition
        self.helper2 = helper2
    
    def do_main_thing(self, param):  # Public behavior
        # Tell helpers what to do
        result = self.helper1.process(param)
        # Update my own state
        self._my_data = result
        return result
    
    def __str__(self):
        return f"Display my state"
```

---

## 🚀 YOUR ACTION PLAN

1. **Design** with the questionnaire
2. **Check** with this 5-principles list
3. **Code** following the Good Student Template
4. **Review** for Red Flags
5. **Submit** with confidence!

**Remember:** Your teacher knows you're learning. Showing that you *tried* to follow OOP principles (even if imperfect) is often more important than perfect implementation. Document your design decisions - "I made Book passive because..." shows understanding!

**Need a specific example for your current assignment?** Show me your teacher's requirements and I'll walk through the checklist with you!