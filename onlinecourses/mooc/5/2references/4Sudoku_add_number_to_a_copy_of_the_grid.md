
This is the very last sudoku task. This time we will create a slightly different version of the function for adding new numbers to the grid.
The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should return a copy of the original grid with the new digit added in the correct location. The function should not change the original grid received as a parameter.
The print_sudoku function from the previous exercise could be useful for testing, and it is used in the example below:
LOGICAL OPERATIONS
    -   copy and add func
        -   receive a list 
        -   receive an int for row 
        -   receive an int for column
        -   receive an int for sudoku cell
        -   create new list its independent copy of the received list
        -   create for loop iterate new list
            -   use row as index for the outer list 
                -   create inner for loop to iterate the list in the index location
                -   use column as index 
                -   in the index location give the cell number as value
        -   OR make copy of an list use : for full copy newlist = [row[:] for row in sudoku]
            -   then new_list[0][0]= 2

    -   print sudoku func
        -   receive a list 
        -   for loop
        -   iterate the list
            -   inner for loop
                -   iterate inner list
                -   for every value that is 0 print '_'
                -   add space after every value 
                -   if the index positions are 2 or 5 add 2 spaces after them 
                -   if the index position is -1 do not add space 
                -   if the value is not 0 print the value 

PATTERNS
# I am beginner tell me correct patterns if I descriped them correctly 
    -   copy and add func
        -   mutate pattern
        -   copy pattern


    -   print sudoku func
        -   transform pattern
        -   iterate pattern 
        -   output pattern



AI patterns 

Missing/More precise patterns:

For copy_and_add:

Defensive copy pattern → Creating a copy to avoid side effects

Grid/indexing pattern → Using row/column coordinates to access 2D structure

Pure function pattern → No side effects, returns new data

For print_sudoku:

Formatting pattern → Adding spaces, special characters for readability

Separation of concerns → Only displays, doesn't modify data

Nested iteration pattern → Working with rows and columns





AI 
Real patterns would be things like:

Factory pattern

Singleton pattern

Observer pattern

Iterator pattern (which actually applies here!)

Strategy pattern