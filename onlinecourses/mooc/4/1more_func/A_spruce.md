Please write a function named spruce, which takes one argument. The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.

Calling spruce(3) should print out

Sample output
a spruce!
  *
 ***
*****
  *
Calling spruce(5) should print out

Sample output
a spruce!
    *
   ***
  *****
 *******
*********
    *
NB: to the left of the spruce there should be exactly the right amount of whitespace. If the shape of the spruce looks correct, but the left edge of the tree is not touching the left edge of the text area in the terminal, the tests will not accept the solution.


1. input = int > 2. func > 3. (loop * int + 1) >4. str > 5. space 

Pattern Recognition Warm-up - Even more crucial with functions
output patter
   1.  (4 space) 1* (4 empty space)
   2.  (3 space) 3* (1) (3 space)
   3.  (2 space) 5* (2 space)
   4.  (1 space) 8* (1 space)
   5.  empty print()
   6.  (4 space) 1* (4 empty space)
pattern
   1.  '*' grows by 2 and space shrinks by 2 
   2.  after all is '*' then it resets to
   3.  * and rest is space


Solution Time Boxing - Functions can lead to over-engineering

"Elegant Solution" Analysis - Critical for learning function design