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
- How does it relate to others? it is stored in the appointment

For EACH doctor:

- What DATA does it need? id, name, specialization
- What ACTIONS can it do? refuse
- How does it relate to others? __________

For EACH appointment:

- What DATA does it need? patient, doctor, datetime, status
- What ACTIONS can it do? ________________
- How does it relate to others? __________

For EACH hospital:

- What DATA does it need? doctors, patients, schedule_appointment(), cancel_appointment()
- What ACTIONS can it do? ________________
- How does it relate to others? __________
-

### **PART 3: DESIGN DECISIONS**

Structure:
[ ] Single class
[ ] Multiple independent classes  
[ ] Classes with inheritance (Parent→Child)
[ ] Classes with composition (Container→Contained)

Communication:
[ ] Direct calls between objects
[ ] Through central coordinator
[ ] Events/messages

Data Storage:
[ ] In-memory only
[ ] Files
[ ] Database (later)

-

### **PART 4: IMPLEMENTATION PLAN**

PHASE 1: Build ________________________
         (Test: Can it ________________?)

PHASE 2: Add _________________________
         (Connects via: _______________)

PHASE 3: Add _________________________
         (Completes: __________________)

STOP CRITERIA: _______________________

-

## **HOW TO USE THIS TEMPLATE:**

1. **Fill in Part 1** with YOUR project specifics
2. **Fill in Part 2** with YOUR objects/concepts  
3. **Make choices in Part 3** for YOUR design
4. **Create a plan in Part 4** for YOUR implementation
5. **THEN** write code based on YOUR answers
