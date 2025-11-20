
Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.

An example of expected behaviour:

first_string = "abcdbde"
print(most_common_character(first_string))

second_string = "exemplaryelementary"
print(most_common_character(second_string))
Sample output
b
e

function takes an string 
it calculates occurence of every letter in the string 
stores total of every letter somehow and then check the max if there is two letters with similar occurence count 
print based on the earlier occurence in the string

init function most_common_character

init storage for the most common value
inti accumulator to store occurences of the letters

init loop

get letter accumualate occurence of the letter

store count of a letters

Track first occurrence position during comparison.?

evaluate if equal counts to max count exist

order by location of occurence in the string

print the letter