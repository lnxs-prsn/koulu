
Please write a function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary. The number is the key, and the factorial of that number is the value mapped to it.

A reminder: the factorial of the number n is written n! and is calculated by multiplying the number by each integer smaller than itself. For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.

An example of the function in action:

k = factorials(5)
print(k[1])
print(k[3])
print(k[5])
Sample output
1
6
120

LOGICAL OPERATIONS 
    -   factorials(n:int)
        -   receives n int
        -   init empty dict
        -   init for loop over the range of n and set the range to start from 1 and go to n+1
            -   factorial: int
            -   storage: int = 2 # can be obtimized by setting to outerindex + 1 incases where outer index is more than 2
            -   if outer index is 1 or if outer index is 2
                -    dict[outerindex]= outerindex
            -   init for loop over range of outer loop index set to start from 2 and to outerloop index 
                -   storage = storage * (innerloop index +1)
                -   #*
                -   factorial = storage
            -   if outer index > 2
                -   dict[outerindex] = factorial
        -   return dict
-   thinking mistakes in logical operations 
    -   if innerloop index == outerloop index # wrong the loop ends before reaching the condition   *