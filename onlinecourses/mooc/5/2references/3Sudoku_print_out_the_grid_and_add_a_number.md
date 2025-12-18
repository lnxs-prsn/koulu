In this exercise we will complete two more functions for the sudoku project from the previous section: print_sudoku and add_number.

The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. The function should print out the grid in the format specified in the examples below.

The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should add the digit to the specified location in the grid.

sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print_sudoku(sudoku)
add_number(sudoku, 0, 0, 2)
add_number(sudoku, 1, 2, 7)
add_number(sudoku, 5, 7, 3)
print()
print("Three numbers added:")
print()
print_sudoku(sudoku)
Sample output
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Three numbers added:

2 _ _  _ _ _  _ _ _
_ _ 7  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ 3 _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Hint

Remember it is possible to call the print function without causing a line change:

print("characters ", end="")
print("without carriage returns", end="")
Sample output
characters without carriage returns

Sometimes you need just a new line, which a print statement without any argument will achieve:

print()



LOGICAL OPERATIONS 
The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. The function should print out the grid in the format specified in the examples below.
    -   init function print_sudoku
    -   receive a list
    -   init loop
    -   iterate outer list
    -   interate inner list 
    -   every element in the inner list transform 0 to '_'
    -   print every element of transformed list in specified format
        -   print 3 elements space then 3 elements then space and the last 3 elements

The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should add the digit to the specified location in the grid.
    -   init function add_number
    -   receive the list
    -   receive the numbers 
    -   direct assignment
        -   take first number as index of outer 
        -   take second number as index for inner list
        -   set third number as value for the index location
    -  


PATTERNS
    PRINT SUDOKU FUNC
       -   transformation pattern
       -   init pattern
       -   iteration pattern
       -   output pattern
       -   

    ADD NUMBER FUNC
       -   init func 
       -   mutation pattern
-   


AI PART OF THE CODE 

CORRECT TERMINOLOGY PATTERNS 
    -   TRANSFORMATION PATTERN
    -   FORMATTER OUTPUT PATTERN
    -   INDEX BASED UPDATE PATTERN

