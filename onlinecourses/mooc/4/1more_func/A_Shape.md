Please write a function named shape, which takes four arguments. 
The first two parameters specify a triangle, as above, and the character used to draw it. 
The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. 
The fourth parameter specifies the filler character of the rectangle. 
The function prints first the triangle, and then the rectangle below it.

The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

Some examples:

shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")
Sample output
X
XX
XXX
XXXX
XXXXX
*****
*****
*****

o
oo
++
++
++
++

.
..
...
Hint

Don't try and solve this exercise "all at once". A good first step would be to make sure you can print the triangle reliably. Then you can try adding the rectangle.

This is one of the most important skills of a programmer: concentrate on small, tangible sections of the problem at a time. Solve and verify partial solutions, and use them to build towards a complete solution.


Input → [Function] → Expected Output

input1 = int, str > func > loop that increases the amount of str > first round str*1 round 2 str*2 until round int str*int
input2 = int, str > func > in loop multiples str*int as many rounds as int so in the last round it print out will be same as in the first round

