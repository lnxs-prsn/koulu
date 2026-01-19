
Please write a phone book application. It should work as follows:
Sample output
command (1 search, 2 add, 3 quit): 2
name: peter
number: 09-22223333
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
09-22223333
command (1 search, 2 add, 3 quit): 3
quitting...
As you can see above, each name can be attached to a single number only. If a new entry with the same name is added, the number attached to the old entry is replaced with the new number.
NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.
Logical operations
    -   phonebook = {}
    -   while true:
        -   ask which input
        -   if choice is 1 search
            -   based on the name and print phone number
        -   if choice is 2 
            -   add to phonebook name as a key and phone number as value and print ok!
        -   if choice is 3 end the loop
            -   print quitting
1. yes
   1. ask which input repeats 
      1. search by name
      2. add to phonebook
2. yes
   1. ask which input repeats 
      1. search by name
      2. add to phonebook
3. yes
   1. if choice 1 
   2. if choice 2
   3. if choice 3
4. yes
5. yes?
6. add either to phonebook or search from the phonebook or close the phonebook
7. storage
   1. add to storage or search from storage
   2. or close the storage

