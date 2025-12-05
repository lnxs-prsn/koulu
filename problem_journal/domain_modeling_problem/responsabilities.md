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


