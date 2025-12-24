### **Exercise A: Coffee Shop** # correct !
# Customer → Order? 
# Order → Barista?
# Barista → CoffeeMachine?
# CoffeeMachine → Coffee?

# Task: Write the METHOD CALLING SEQUENCE for:
# 1. Customer places order
    -   customer calls barista, barista calls order, 
# 2. Barista makes coffee
    -   barista calls coffee machine, 
# 3. Customer receives coffee
    -   barista call customer
# Focus: Which object's method calls which other object's method?
all calls go throught the barista as its coordinator