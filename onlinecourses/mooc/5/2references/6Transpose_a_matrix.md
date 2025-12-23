Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. The function should transpose the matrix. Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.

You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.

The following matrix

1 2 3
4 5 6
7 8 9
transposed looks like this:

1 4 7
2 5 8
3 6 9
The function should not have a return value. The matrix should be modified directly through the reference.


what I need to do
            -   put first inner list values to fill the index position 0 
            -   then second list values fill the index position 1
            -   and lastly make the last list fill the index position 2

presently in mind idea 
locationx , locationy = valuelocationy, valuelocationx
have index x and index y
put in to loop 
iterate
x stays constant        y stays constant
listlocation[y][x],  listlocation[x][y]= listlocatin[x][y],listlocation[y][x]
so take values from one list exchange them with the other in place 

LOGICAL OPERATIONS
    -   transpose func
        -   receive list
        -   create x index int
        -   create y index int
            -   outer for loop
                -   inner for loop
                    -   the element in the outer list index 0 and and inner list index 1 
                    -   is swapped with the element in the outer list index 1 and and inner list index 0 
                    -   if the element index in the inner list is bigger than the element index in the outer list
                    -   OR loop the inner list based on cases when its inner index than the outer loop index




PATTERN
    -   The pattern was: “All necessary changes live in the upper triangle of a symmetric grid.”
    -   index based swapping
    -   in place mutation
-   


AI CORRECTED PATTERN
    -   Triangular traversal

GENERALIZED SOLUTION
    -   for j in range(i + 1, n)
        -   matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

