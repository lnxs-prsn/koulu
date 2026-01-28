
Please write a function named dict_of_numbers(), which returns a new dictionary. The dictionary should have the numbers from 0 to 99 as its keys. The value attached to each key should be the number spelled out in words. Please have a look at the example below:

numbers = dict_of_numbers()
print(numbers[2])
print(numbers[11])
print(numbers[45])
print(numbers[99])
print(numbers[0])
Sample output
two
eleven
forty-five
ninety-nine
zero

NB: Please don't formulate each spelled out number by hand. Figure out how you can use loops and dictionaries in your solution.
LOGICAL OPERATIONS
    -   dict_of_numbers()
        -   empty dict
        -   dict_of_0_to_9
            -   stores spelled out numbers from 0 to 9
        -   dict_10_to_19
            -   stores the spelled numbers between 10 and 109
            -   stores only spelled out tens from 20 to 90
        -   for loop in range of 0-100
            -   if x in keys dict_of_0_to_9
                -   set x as key and dict_of_0_to_9[x] as value in the empty dict
            -   elif x in dict_10_to_19
                -   set x as key and dict_of_10_to_19[x] as value in the empty dict
            -   else
            -   if 
                -   take shalow copy of x1 = x and convert to str
                    -   first = x1[0] back to num
                    -   second = x1[1] convert back to num
                -   if second is not 0
                    -   set x as key for empty dict and dict_od_tens[first]+dict_of_0_9[second]
                -   else
                    -   set x as key for empty dict and dict_od_tens[first]
1. yes
   1. if/else repeat constantly
   2. setting key and value repeats constantly
2. yes
   1. if/else 
   2. setting key and value on empty dict
3. yes 
4. yes
5. yes
6. yes
   1. build from preset words new words and set them as values to dict
7. yes
   1. set storage 
   2. set up a template
   3. run range of numbers through template
   4. build dictionary out of the number and the output of the template