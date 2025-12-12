who is the authority of the action

EXAMPLE
# Actions: Library lends books to members
    -   THE LIBRARY IS THE AUTHORITY
        -   IT IS USING THE VERB lENDS SO ITS THE AUTHORITY
-   

QUESTION IS SIMPLE 
    -   WHERE IS THE BUSINESS LOGIC THERE IS THE AUTHORITY

AUTHORITY
    -   Who everyone points fingers at if something goes wrong 
    -   who points finger when things go wrong.

AUTHORITY DEPENDECY?
    -   is there 
        -   strong lifecycle dependency?

WHO CONTROL CREATION AND ASSIGNMENT
    -   in object design, 
        -   who controls creation and assignment 
            -   determines authority.





1. Library Circulation System
Build a system that tracks which books are checked out to which members, enforces borrowing limits, and prevents invalid operations (like checking out an unavailable book). Use no more than three classes.


ACTIONS
   -   library borrows books 


PARTICIPANTS 
   -   library
   -   member
   -   book


RESPONSABILITIES
   -   library 
       -   coordinates the books and members 
           -   there is never book for member that does not exist 
           -   there is never for a member a book that does not exist
   -   member
       -   stores data initiates action of borrowing
           -   name, address etc
   -   book
       -   stores data
       -   knows its author, its content, stores its state borrowed or not 

AUTHORITY
   -   library 
       -   is the authority in charge of all motion except initial request
   -   book
       -   participant
           -   acted on 
   -   member
       -   participant
           -   acted on