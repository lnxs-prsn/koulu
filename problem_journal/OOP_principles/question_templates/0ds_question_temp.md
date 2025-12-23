Perfect! I understand completely. You're a student learning OOP and you want a **guided question process** that takes you from a teacher's assignment to a ready-to-implement OOP design.

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

## EXAMPLE: LIBRARY SYSTEM (Filled Out)

**STEP 1:** 
- Nouns: Books, Members, Loans, Library
- Verbs: Borrow, Return, Search, Register

**STEP 2:**
- Classes: Book, Member, Library (active), Loan (passive)
- Active: Library, Member | Passive: Book, Loan

**STEP 3:**
- Library KNOWS: books list, members list | DOES: lend_book(), return_book()
- Member KNOWS: name, borrowed_books | DOES: borrow_book(), return_book()
- Book KNOWS: title, author, is_available | DOES: get_info(), mark_borrowed()

**STEP 4:**
- Library HAS-A list of Books (composition)
- Library USES Member (dependency)
- Coordinator: Library (creates/manages everything)

**STEP 5:**
- Library: add_book(), register_member(), lend_book(), return_book()
- Member: get_info(), show_borrowed_books()
- Book: get_info(), is_available()

**STEP 6:**
1. Member comes to library
2. Library checks if member is registered
3. Member requests a book
4. Library checks if book is available
5. Library creates loan record
6. Library updates book and member status

**STEP 7:**
```python
class Library:
    """Manages books and members in a library"""
    
    def __init__(self):
        self._books = []
        self._members = []
    
    def lend_book(self, member_name, book_title):
        """Lend a book to a member"""
        # 1. Find member
        # 2. Find book  
        # 3. Check if book available
        # 4. Update both
        pass
```

---

## HOW TO USE THIS:

1. **Get your assignment** from teacher
2. **Print this questionnaire** or copy to a document
3. **Work through each step** - don't skip!
4. **Show your answers** to teacher for feedback
5. **Then start coding** - you'll know exactly what to write

**Remember:** There's no single "right" answer in OOP. Different designs can work. The important thing is that your design makes sense and you can explain your choices.

**Do you want me to create a Python script that asks these questions interactively?** That could guide you through the process step-by-step on your computer!