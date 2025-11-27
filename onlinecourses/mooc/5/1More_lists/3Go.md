In a game of Go two players take turns to place black and white stones on a game board. The winner is the player who manages to encircle a bigger area on the board with their own game pieces.

Please write a function named who_won(game_board: list), which takes a two-dimensional array as its argument. The array consists of integer values, which represent the following situations:

0: empty square
1: player 1 game piece
2: player 2 game piece
The scoring rules of Go can be quite complex, but in this exercise it is enough to compare the number of pieces each player has on the game board. Also, the size of the game board is not limited.

The function should return the value 1 if player 1 won, and the value 2 if player 2 won. If both players have the same number of pieces on the board, the function should return the value 0.

PROBLEM REWORDING
task wants me to make an function
    -   function takes an list which is snap shot of the game situation 
    -   and it wants me to calculate how many squeres player 1 occupies 
    -   and how many squeres player 2 occupies 
    -   then compare which player occupies more 
-   

LOGICAL OPERATIONS
    -   init func
    -   init loop 
    -   iterate rows 
    -   init loop 
    -   iterate elements in the list
    -   check if the element value
    -   then increment correct counter based on value
    -   after loop compare which has more player 1 or player 2
    -   return 1,2,0 according to comparison
-   

PATTERNS
    -   init pattern
    -   iteration pattern
    -   accumulation pattern
    -   check and comparison pattern
    -   output pattern