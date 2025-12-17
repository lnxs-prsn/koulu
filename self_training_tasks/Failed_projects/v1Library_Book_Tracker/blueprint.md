

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
       -   participant/initiator of the borrowing process
           -   acted on


ARROWS 
   -   library > book and library > member
   -   initiation flow
       -   member > library then library > book and finally library > member


CONSTRAINS
   -   cannot borrow 
       -   non existing book, already borrowed book
   -   cannot borrow to 
       -   member with too many books, non member, 
   -   can borrow 
       -   existing book, available book
   -   can borrow to 
       -   member, member with space to borrow more 



DESIGN DECSIONS
   -   library
       -   toggles the states of the book object 
           -   borrowed/ available
       -   toggles the states of he member object using methods of the object itself
           -   can borrow / cannot borrow
   -   member 
       -   stores states and user data
       -   has method  request book for borrowing
       -   has state can_borrow boolean  returns boolean
       -   has int variable total_books borrowed
   -   book
       -   stores data related to book and its states
       -   has method borrow which changes the state
       -   has method to check state
       -   has state available boolean
-   

