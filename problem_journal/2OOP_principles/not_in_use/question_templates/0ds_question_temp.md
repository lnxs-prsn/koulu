Here's a **7-Step OOP Design Questionnaire** for students. When you get a Python OOP assignment from your teacher, work through these questions step by step:

---

# OOP DESIGN QUESTIONNAIRE FOR STUDENTS
**Project:** [Your Assignment Name]

## STEP 1: UNDERSTAND THE REQUIREMENTS
**Q1:** What are the main things in this system? (Nouns)
```
Example: Library → Books, Members, Loans
Your answer: _________________________________________
```

**Q2:** What should the system do? (Verbs/Actions)
```
Example: 
- Borrow books
- Return books  
- Search for books
Your answer: _________________________________________
```

## STEP 2: IDENTIFY THE OBJECTS
**Q3:** Which nouns become classes?
```
Rule: If it has data AND behavior, make it a class.
Example:
- Book: has title/author, can be borrowed/returned → YES
- LibraryCard: has number, expiration date → YES  
- Address: just data → NO (use string or dataclass)
Your classes: _________________________________________
```

**Q4:** Which classes are "active" (do things) vs "passive" (hold data)?
```
Active: Does actions, coordinates, validates
Passive: Holds data, gets acted upon
Your classification:
- Active: ________________
- Passive: _______________
```

## STEP 3: ASSIGN RESPONSIBILITIES
**Q5:** For EACH class, answer:
1. **What does it KNOW?** (data/state)
2. **What does it DO?** (methods/behavior)

```
Example for Book class:
KNOWS: title, author, is_borrowed, borrower
DOES: get_info(), mark_borrowed(), mark_returned()

Fill for your classes:
[Class 1]: KNOWS ________________, DOES ________________
[Class 2]: KNOWS ________________, DOES ________________
[Class 3]: KNOWS ________________, DOES ________________
```

## STEP 4: FIND RELATIONSHIPS
**Q6:** How do objects work together?
```
Ask: "Who needs who?"
- Composition: HAS-A (Library has Books)
- Dependency: USES-A (Library uses Member)
- No relationship: Independent objects

Your relationships:
[Class A] _________ [Class B] because ________________
```

**Q7:** Who is the "boss"/coordinator?
```
The coordinator:
1. Creates other objects
2. Validates rules
3. Tells objects what to do

Your coordinator: ________________ because ________________
```

## STEP 5: DESIGN THE METHODS
**Q8:** What are the 3-5 most important methods for each class?
```
Keep it simple! 3-5 methods max per class.

[Class 1]:
1. ________________ (does what?)
2. ________________
3. ________________

[Class 2]:
1. ________________
2. ________________
3. ________________
```

## STEP 6: PLAN THE FLOW
**Q9:** What's the main sequence when someone uses the system?
```
Example: Library system
1. Member shows card
2. Library validates card
3. Member asks for book
4. Library checks if book available
5. Library marks book borrowed
6. Library updates member's borrowed list

Your main flow:
1. ________________
2. ________________  
3. ________________
4. ________________
```

## STEP 7: SKETCH THE CODE
**Q10:** Write skeleton code for ONE key class:
```python
class [YourClassName]:
    """One sentence: what this class does"""
    
    def __init__(self, [parameters]):
        """What data does it need to start?"""
        self._data1 = data1  # _ means "private"
        self._data2 = data2
    
    def main_action(self, param):
        """What's the most important thing it does?"""
        # 1. Check something
        # 2. Update self
        # 3. Return result
        pass
    
    def __str__(self):
        """How should it display as string?"""
        return f"[display format]"
```

---
