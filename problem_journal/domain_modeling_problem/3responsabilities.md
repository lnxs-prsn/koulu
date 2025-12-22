what are passive in object responsabilities ?

what are active cross object boundary responsabilites 
    EXAMPLE : 
        -   # Actions: Library lends books to members
            -   LIBRARY 
                -   KNOWING RESPONSIBILITES 
                    -   list of books
                    -   list of members
                -   DOING RESPONSIBILITES
                    -   COORDINATE BOOK AND MEMBER OBJECTS
                        -   tell book its borrowed
                        -   tell member they have borrowed it
                        -   enforce rules when to return 
                        -   max borrowing 
            -   BOOK 
                -   KNOWING RESPONSIBILITES
                    -   KNOW THE DETAILS OF THE BOOK
                        -   author, title, is borrowed?
                -   DOING RESPONSIBILITES
                    -   NONE
            -   MEMBER
                -   KNOWING RESPONSIBILITES
                    -   KNOW THE DETAILS OF MEMBER
                        -   name, address, what has borrowed
                -   DOING RESPONSIBILITES
                    -   NONE

WHICH OBJECT IS RESPONSIBLE FOR CREATING OTHER OBJECTS
    -   EXAMPLE
        -   if there are library, book, member objects 
            -   library is responsible for creating the other objects
                -   it has responsibility to know who can borrow and what can be borrowed.

 Rule of thumb:
    -   If system has a closed world (only certain entities are valid),
        -   then creation must be controlled.
    -   If it’s an open world (any instance is valid), then free creation is fine.

coordinator is responsible for validation when gatekeeping
    -   who ever coordinates, library, bank, school etc
        -   must validate the gateway before the action
            -   age, amount of resources, value etc
        -   objects themselves are acted on so they cannot be gatekeepers
            -   deciding who can interact with them
            -   only coordinator can
            -   BUT objects can validate their own data integrity
                -   


coordinator tells objects what to do 
    -   they take actions themselves 
        -   if something needs to be removed added etc
            -   objects do it themselves coordinator tells when to do
            -   what is done by the objects when is commanded by the coordinator
            -   "If an action needs validation, the coordinator MUST validate it BEFORE commanding any participants to act."




