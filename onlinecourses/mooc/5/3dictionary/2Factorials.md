
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
        -   init factorial 1
        -   init for loop over the range of n and set the range to start from 1 and go to n+1
            -   factorial = factorial * index 
            -   dict[index] = factorial
        -   return dict
-   thinking mistakes in logical operations 
    -   if innerloop index == outerloop index # wrong the loop ends before reaching the condition   *



PATTERNS
    -   what are invariants
        -   process is constant accumulation through multiplication
            -   (((x)*(y))*(z))*(v)
            -   after the x and y the z is determined by the sum of x and y and v is determined by the sum of xyz etc


AI PATTERNS (WITH THE 7 QUESTION TEMPLATE)
    -   Cumulative product pattern: Each result builds on the previous one by multiplying the next integer.
    -   Uniform iteration: The same operation applies to every item — no true special cases.
    -   Single-pass accumulation: No need to recompute from scratch; one loop suffices.
    -   State-carrying loop: A running value (factorial) is updated and stored at each step.
    -   Sequential dependency: The value for k depends directly on the value for k−1.