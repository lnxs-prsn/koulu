# SCENARIO 1: Library System
# Objects: Library, Book, Member
# Actions: Library lends books to members

# Draw arrows between:
# Library → Book ?
# Library → Member ?
# Book → Library ?
# Book → Member ?
# Member → Library ?
# Member → Book ?

# SCENARIO 2: Restaurant Ordering
# Objects: Customer, Waiter, Kitchen, Order
# Actions: Customer gives order to waiter, waiter sends to kitchen

# Draw arrows between all pairs




AUTHORITY
# Actions: Customer gives order to waiter, waiter sends to kitchen
    -   CUSTOMER IS THE ATHORITY 
        -   IT IS USING THE VERB GIVES ORDER 
        -   AUTHORITY HAS HIERACHY 
            -   customer > order > waiter > kitchen


# Actions: Customer gives order to waiter, waiter sends to kitchen

CUSTOMER
-   calls object tells gives it arguments as what it wants 

ORDER 
-   receives instructions from customer
-   calls waiter to deliver instruction to kitchen  # this breaks the rules that every object needs to minds its business unless its the authority 
    -   this stores states and calls out 
-   

WAITER
-   receives the instructions from order # this is wrong 
-   calls the kitchen and tells the instructions # this is wrong 
-   


intuition tells me that 
the centr is the Waiter 
talks with customer, talks with order, talks with kitchen 
but as the rules are still not clear am bit confused

