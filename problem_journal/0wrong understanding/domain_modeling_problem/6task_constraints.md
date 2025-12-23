Defining task constraints is about stating what must never be violated, 
independent of how you code it.

A task constraint is a rule that must always be true before, during, or after an action.

Think of them as:
Invariants (must always hold)
Preconditions (must be true before action)
Postconditions (must be true after action)

2. How to define them (step-by-step method)
Step 1: Pick an action
Example: borrow book

Step 2: Ask 3 questions
A. What must be true before the action?
(preconditions)
Examples (conceptual, not code): Member exists, Book exists, Book is not already borrowed,
Member has not exceeded borrowing limit

B. What must never happen?
(invariants)
Examples:
A book cannot be borrowed by two members, A member cannot borrow a non-existent book, Borrow count cannot be negative,
Library cannot reference unknown members or books

C. What must be true after the action?
(postconditions)
Examples:
Book is marked as borrowed, Book is linked to exactly one member, Member’s borrowed count increases by one
Library state remains consistent



How to define task constraints:
Choose an action
Define preconditions
Define invariants
Define postconditions
Assign enforcement to the responsible class

Constraints belong to the authority class.





