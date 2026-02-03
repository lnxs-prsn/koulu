
Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. In each tuple, the first element is the name of a person, and the second element is their year of birth. The function should find the oldest person on the list and return their name.
An example of the function in action:
p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]
print(oldest_person(people))
Sample output
Mary
LOGICAL OPERATIONS
    -   oldest_person(people:list)
        -   smallest: int
        -   for loop
            -   if tuple[1] is smaller than smallest
                -   set tuple[1] as smallest else continue 
        -   after loop return smallest
        -   return min(people, key=lambda x: x[1])
1. yes
   1. iteration of every tuple and comparing to smallest
2. yes
   1. iteration of every tuple and comparing to smallest 
3. yes
   1. comparing to smallest has if else statement
4. yes
   1. its loop
5. yes
   1. am comparing to smallest
6. yes
   1. inplace iteration and comparison
7. yes
   1. iterate through data structures based on index
   2.  compare values in index location
   3. return smallest