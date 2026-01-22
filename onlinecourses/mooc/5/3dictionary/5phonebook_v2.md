Please write an improved version of the phone book application. Each entry should now accommodate multiple phone numbers. The application should work otherwise exactly as above, but this time all numbers attached to a name should be printed.

Sample output
command (1 search, 2 add, 3 quit): 2
name: peter
number: 040-5466745
ok!
command (1 search, 2 add, 3 quit): 2
name: emily
number: 045-1212344
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
040-5466745
command (1 search, 2 add, 3 quit): 1
name: mary
no number
command (1 search, 2 add, 3 quit): 2
name: peter
number: 09-22223333
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
040-5466745
09-22223333
command (1 search, 2 add, 3 quit): 3
quitting...
LOGICAL OPERATIONS
    -   empty dict
    -   while loop
        -   if user choice is 1 
            -   search by name and print all the phone numbers
        -   if choice is 2
            -   if name does not exist add name then add phone numbers 
            -   if name exists add phone number
            -   print ok! at the end
        -   if choice is 3 
            -   break out of the loop
    -   print quitting...
1. yes
   1. choosing options repeat
2. yes 
   1. if choice is 1 then action 1 follows 
   2. if choice is 2 then action 2 follows 
3. yes
   1. there is if else when checking what to do based on user choices
4. yes but with limitedly
   1. user choosing what to do repeats 
   2. choice 1 can repeat and also choice 2 can repeat 
   3. choice 3 happens only once
5. no
6. yes
   1. store users name and phone numbers to phone book, search user by name in the phone book
7. yes
   8. store to and retrieve from the storage by condition