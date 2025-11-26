I TRIED TO SOLVE AND TASK OF !!find the maximum number of consecutive difference-of-1 pairs!!
INSTEAD OF SOLVING THE TASK MOOC GAVE ME

I DONT YET KNOW WHAT OCCURED BUT I WAS SOLVING AN WRONG TASK LUCKILY SOLUTIONS ARE VERY CLOSE





Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1. So, items 1 and 2 would be neighbours, and so would items 56 and 55.

Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.

For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.

An example function call:

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))



LOGICAL OPERATIONS

init func
receive list
store max consequtive 
init loop
check if concequetive elements difference 
if difference 1 increment max 
store all the consequetive neighbours length to list 
return max length


PATTERNS
init pattern
accumulation pattern
iterations pattern
evaluate pattern
max value track pattern
current state tracking pattern
reset pattern


!!! SOLUTION! PROBLEM IS THAT THIS IS TASK SEARCHES CONSEQUENTIVE SEQUENCE AND CONSEQUETIVE SEQUENCE ALWAYS STARTS 
FROM 1. 

I WOULD HAVE NEEDED AND AN VARIABLE THAT IS INITIATED WITH 1 TO STORE RUNNING CURRENT