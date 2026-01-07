Please write a function named histogram, which takes a string as its argument. The function should print out a histogram representing the number of times each letter occurs in the string. Each occurrence of a letter should be represented by a star on the specific line for that letter.
For example, the function call histogram("abba") should print out
Sample output
a **
b **

LOGICAL OPERATIONS
    -   init func(string:str)   # this is pure function no change happens to input and nothing is returned
        -   init a loop in range of set(string)
            -   count letter in the string 
            -   print letter + * total
1. yes
   2. count letter in the string 
   3. print letter + * total
2. yes
   2. count letter in the string 
   3. print letter + * total
3. no
4. yes
5. yes
6. yes
   1. print letter + count total multiplied by '*'
7. yes # correct “Aggregate → Transform → Display”
   1. traverse a string 
   2. count element total appearance
   3. print letter + total* '*'