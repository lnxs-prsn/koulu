start from logical operations of the problem
from the logical operations derive patters 





Please write a function named block_correct(sudoku: list, row_no: int, column_no: int), which takes a two-dimensional array representing a sudoku grid, and two integers referring to the row and column indexes of a single square, as its arguments. Rows and columns are indexed from 0.

The function should return True or False depending on whether the 3 by 3 block to the right and down from the given indexes is filled in correctly. That is, whether the block contains each of the numbers 1 to 9 at most once.

Notice that this function does not strictly follow the rules of sudoku. In a real game of sudoku there are only 9 blocks to check, and these are located at indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6). Such restrictions on indexes should not be implemented here.

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(block_correct(sudoku, 0, 0))
print(block_correct(sudoku, 1, 2))
Sample output
False
True

The first function call should check the 3 by 3 block beginning with the square at indexes 0, 0:

9 0 0
2 0 0
0 2 0
The second function call should check the 3 by 3 block beginning with the square at row 1, column 2:

0 2 5
0 3 0
4 0 0
This second block would not be checked in an actual game of sudoku, but your function should allow for it to be checked.

REWORDING PROBLEM
    -   function takes a list and two int values
    -   the two int values are the starting point of the 3 by 3 block of numbers
    -   so with example 0,0 values 
        -   in the outer loop print only 3 inners list from 0-2
        -   and in the inner loop print elements from 0-2
-   

LOGICAL OPERATIONS
    -   init func
    -   receive list, num 1 and num 2
    -   new list to store the block
    -   bool variable set to True
    -   init loop set outer list to print 3 rows only start from first num1
    -   get 3 elements from inner list starting from num2 as index location
    -   store to a variable
    -   check and compare if values have repetition in the 3x3 block
    -   return true or false according to check and compare
    -   
-   

PATTERNS
    -   init pattern
    -   iteration pattern
    -   acumulation pattern
    -   check and compare pattern
    -   validation pattern
    -   return pattern
