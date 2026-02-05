
In this exercise we are handling tuples just like the ones described in the previous exercise.
Please write a function named older_people(people: list, year: int), which selects all those people on the list who were born before the year given as an argument. The function should return the names of these people in a new list.
An example of its use:
p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]
older = older_people(people, 1979)
print(older)
Sample output
[ 'Adam', 'Mary' ]
LOGICAL OPERATIONS 
    -   older_people(people: list, year: int)
        -   new_list: list
        -   iterate people lists tuples second index
        -   with condition if less than year add tuples first index to new_list
        -   return new_list
1. yes
   1. conditional filtering 
2. yes
   1. filter match
3. yes
   1. is there less than value
4. yes
   1. test stays same if there is match accumulation occurs in new list
5. yes
   1. am doing same kind of things to different items
6. yes
   1. accumulate items matching condition
7. yes
   1. iterate, filter, accumulate