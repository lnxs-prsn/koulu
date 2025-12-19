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
listlocation[x][y] = listlocatin[x][y]
so take values from one list exchange them with the other in place 

LOGICAL OPERATIONS
    -   transpose func
        -   receive list
        -   create x index int
        -   create y index int
            -   for loop 
                -   make exhange of locations 
                    -   make 3 if statements