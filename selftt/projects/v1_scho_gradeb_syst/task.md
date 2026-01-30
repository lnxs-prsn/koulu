

8. School Gradebook System
Purpose: Track students, courses, and grades.
Classes:

Student (id, name, enrolled_courses)

Course (code, name, instructor)

Assignment (course, name, max_score)

Grade (student, assignment, score)

Gradebook (courses, calculate_gpa(), generate_report())

Core Challenge: Maintain grade consistency, calculate weighted averages, and enforce enrollment limits.

# **Python OOP Design Thinking Template** (No Code)

## **PROJECT ANALYSIS FRAMEWORK**

### **PART 1: UNDERSTAND THE PROBLEM**

What REAL-WORLD thing/process am I modeling?
school grading system

What's the SIMPLEST possible version that would work?
course that has an code, name and instructor

What should users be able to DO?

1. :sign up for a course
2. :enroll as a student
3. :do course asignment
4. get grades for their assignment
5. get grade book for all their courses

-

### **PART 2: IDENTIFY CORE COMPONENTS**

What are the main "things" involved?
• course (most important)
• student
• assignment
• grade
• gradebook


For EACH course:

- What DATA does it need? code, name, instructor
- What ACTIONS can it do? change_instructor()
- How does it relate to others? stored or referenced in the student, assignment and gradebook

For EACH student:

- What DATA does it need? id, name, enrolled_courses
- What ACTIONS can it do? enroll_to_course (this method ensures that student cannot enroll more than max allowed courses)
- How does it relate to others? it stores list of courses, its stored in the grade

For EACH assignment:

- What DATA does it need? course, name, max_score
- What ACTIONS can it do? nothing
- How does it relate to others? its stored in the grade

For EACH grade:

- What DATA does it need? student, assignment, score
- What ACTIONS can it do? calculate_score() (this method takes weight the assignment has)
- How does it relate to others? it stores assignment and grade book might call its method

For EACH gradebook:

- What DATA does it need? courses, 
- What ACTIONS can it do? calculate_gpa(), generate_report()
- How does it relate to others? it stores list of existing courses,

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


Answer: course that has an code, name and instructor

Therefore Phase 1 must build: course

STEP 2: Map DEPENDENCIES from Core Components
From PART 2: What depends on what?

course depends on nothing

student depends on course

assignment depends on course

grade depends on student and assignment

gradebook depends on course


Therefore build order: course >student >assignment >grade >gradebook

STEP 3: Determine COMMUNICATION PATTERN
From PART 3: How will objects talk?

Direct calls = Objects interact immediately



Therefore connection method: direct calls

STEP 4: Address CORE CHALLENGE
From Problem Statement: What's the hardest part?


Challenge: calculate weighted averages

Therefore final phase must handle: calculate weighted averages

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

PHASE 1: Build course
         (Test: it has an code, name and instructor?)

PHASE 2: Add student
         (Connects via: direct call)

PHASE 3: Add assignment
         (Completes: calculate weighted averages)

STOP CRITERIA: 
1. :sign up for a course
2. :enroll as a student
3. :do course asignment
4. get grades for their assignment
5. get grade book for all their courses


## **HOW TO USE THIS TEMPLATE:**

1. **Fill in Part 1** with YOUR project specifics
2. **Fill in Part 2** with YOUR objects/concepts  
3. **Make choices in Part 3** for YOUR design
4. **Create a plan in Part 4** for YOUR implementation
5. **THEN** write code based on YOUR answers
