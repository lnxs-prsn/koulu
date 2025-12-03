
1. Transformation Pattern
(Used in print_sudoku: 0 → '_')

Logical operations:

Receive the grid (list of lists of integers)
For each element during printing:
Check if value is 0
If yes, use '_' for display
If no, use the digit itself
Do not modify the original grid
🔑 Core logic: value mapping based on condition (0 → '_'), applied per element

2. Formatted Output Pattern
(Used in print_sudoku: spacing, grouping, newlines)

Logical operations:

Iterate through each row
For each column in the row:
Print the transformed symbol ('_' or digit)
After column 2 and column 5, print an extra space (to separate 3x3 blocks)
After each row, print a newline
After every 3 rows (rows 2 and 5), print an extra blank line (as seen in sample output)
🔑 Core logic: output formatting with positional rules (every 3rd column/row)

3. Index-Based Update Pattern
(Used in add_number: place a number at given row/column)

Logical operations:

Receive the grid, row index, column index, and number
Directly assign: sudoku[row_no][column_no] = number
Assume inputs are valid (per problem statement)
No return value (function modifies grid in place)
🔑 Core logic: direct mutation of a 2D array at specified coordinates

