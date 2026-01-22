Please write a function named invert(dictionary: dict), which takes a dictionary as its argument. The dictionary should be inverted in place so that values become keys and keys become values.
An example of its use:
s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
invert(s)
print(s)
Sample output
{"first": 1, "second": 2, "third": 3, "fourth": 4}
NB: the principles regarding lists covered here also hold for dictionaries passed as arguments.
If you have trouble completing this exercise, the visualisation tool might help you understand what your code is or isn't doing.
LOGICAL OPERATIONS
    -   invert(dictionary:dict)
    -   store the keys and values to list
    -   clear the dictionary
        -   for loop
            -   iterate over stored keys and values
            -    dictionary[value] = key
1. yes
2. yes
   1. iterate over key and value
   2.  dict[value]= key
3. no
4. yes
5. no
6. yes
   1. fake inplace swap of dictionary keys and values 
7. yes
   1. store data of datasctructure accordingly
   2. reset data structure
   3. iterate data
   4. reverse positions of of pointer and data
   5. store reversed pointer and data