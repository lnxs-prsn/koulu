start from logical operations of the problem
from the logical operations derive patters 

TRY TO LEARN CORRECT PATTERN TERMINOLOGY
    -   long term goal no rush!

CORE OF PATTERN RECOGNITION
    -   The habit of interrogating MY own examples for invariant structure.
    -   An invariant is something that stays the same across all cases 
        -    the unchanging core beneath surface differences.
   -    "why this and not that? is there something forcing it to be this way?"



1. Do any steps repeat?
(Exactly the same? Or almost the same with just a small change?)
2. Do some steps always happen together?
(Like: “check something → do something → record result” — does that trio show up more than once?)
3. Is there a “if this, then that” part that shows up often?
(Same kind of choice happening in different places?)
4. Does the process go: Step A → Step B → Step C… and then start over with new info?
(Like a cycle or loop?)
5. Are you doing the same kind of thing to different items?
(For example: “look at voter 1 → count vote → save. Then look at voter 2 → count vote → save…”)
6. Can you describe a group of steps in one short sentence?
(If yes, that’s probably a pattern or a chunk you can reuse.)
7. If you covered up the details, would the shape of the process look familiar?
(Like: “check → act → move on” or “gather → decide → respond”)



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
                -   if innerloop index == outerloop index
                    -   factorial += storage
            -   if outer index > 2
                -   dict[outerindex] = factorial
        -   return dict



PATTERNS
    -   what are invariants
        -   the growth process is constant
            -   (((x)*(y))*(z))*(v)
            -   after the x and y the z is determined by the sum of x and y and v is determined by the sum of xyz etc
            -   