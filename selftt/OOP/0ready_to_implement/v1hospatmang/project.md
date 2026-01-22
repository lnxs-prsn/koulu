5. Hospital Patient Management
Purpose: Track patients, doctors, and appointments.
Classes:
Patient (id, name, medical_history)
Doctor (id, name, specialization)
Appointment (patient, doctor, datetime, status)
Hospital (doctors, patients, schedule_appointment(), cancel_appointment())
Core Challenge: Handle appointment conflicts (same doctor/time) and maintain patient-doctor relationships.
# **Python OOP Design Thinking Template** (No Code)
## **PROJECT ANALYSIS FRAMEWORK**
### **PART 1: UNDERSTAND THE PROBLEM**

What REAL-WORLD thing/process am I modeling?
patiens that come to hospital doctors and appointment of the doctors

What's the SIMPLEST possible version that would work?
patient that can get an appointment
doctor that can receive patient
appointment that can record meeting of doctor and patient
hospital that can house meeting of doctor and patient given time

What should users be able to DO?

1. :create patient and doctor 
2. :get appointment set between doctor and patient
3. :store results of the meeting

-

### **PART 2: IDENTIFY CORE COMPONENTS**

What are the main "things" involved?
• patient (most important)
• doctor
• appointment
• hospital


For EACH patient:

- What DATA does it need? id, name, medical_history
- What ACTIONS can it do? request_appointment
- How does it relate to others? it is stored in the appointment and in the hospital

For EACH doctor:

- What DATA does it need? id, name, specialization
- What ACTIONS can it do? refuse
- How does it relate to others? is stored in the appointment and hospital

For EACH appointment:

- What DATA does it need? patient, doctor, datetime, status
- What ACTIONS can it do? set_appointment(patient,doctor, datetime, status)
- How does it relate to others? referenced by the doctor and patient stored in the hospital

For EACH hospital:

- What DATA does it need? doctors, patients,
- What ACTIONS can it do?  schedule_appointment(), cancel_appointment()
- How does it relate to others? stores doctor, patient, stores doctor
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

Answer: patient that can get appointment

Therefore Phase 1 must build: appointment

STEP 2: Map DEPENDENCIES from Core Components
From PART 2: What depends on what?

appointment depends on patient

hospital depends on doctor



Therefore build order: 1 → 2 → 3

STEP 3: Determine COMMUNICATION PATTERN
From PART 3: How will objects talk?


Coordinator = Objects go through middleman


Therefore connection method: coordinator

STEP 4: Address CORE CHALLENGE
From Problem Statement: What's the hardest part?

Challenge: 2 appointment at same time and doctor patient relationship

Therefore final phase must handle: rules of appointment

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

PHASE 1: Build patient
         (Test: Can it store patient data?)

PHASE 2: Add appointment and hospital
         (Connects via: hospital coordination)

PHASE 3: Add doctor
         (Completes: system)

STOP CRITERIA: 
appointment can store doctor and patient and its state can be toggled
hospital can cancel appointment
patient can store user data 
doctor can store doctor data
-

## **HOW TO USE THIS TEMPLATE:**

1. **Fill in Part 1** with YOUR project specifics
2. **Fill in Part 2** with YOUR objects/concepts  
3. **Make choices in Part 3** for YOUR design
4. **Create a plan in Part 4** for YOUR implementation
5. **THEN** write code based on YOUR answers
