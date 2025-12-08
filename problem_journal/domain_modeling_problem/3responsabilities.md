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
-   





# Airline → Flight? (Airline operates flights)
# Flight → Airline? (Flight is operated by airline)
# Flight → Passenger? (Flight has passengers)
# Passenger → Flight? (Passenger books flights)



ACTION
    -   airline operates
    -   flight is coordinated by airlines
    -   flight stores data of passenger
        -   passengers are assigned to flight
    -   passenger books flight
        -   passenger initiates  
            -   paradoxically real initiator is the airlines by offering a flight
            -   but they offer because passengers have shown interest


PARTICIPANTS
    -   airline
    -   flight 
    -   passenger


RESPONSIBILITIES
    -   airline 
        -   creates flights and coordinates flights and customers
    -   