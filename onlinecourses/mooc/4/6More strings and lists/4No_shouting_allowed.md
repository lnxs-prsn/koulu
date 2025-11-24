Please use the isupper method to write a function named no_shouting, which takes a list of strings as an argument. The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.

An example of expected behaviour:

my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
pruned_list = no_shouting(my_list)
print(pruned_list)
Sample output
['def', 'lower', 'another lower', 'Capitalized']



LOGICAL OPERATIONS
init func
init new empty list
receive a list
iterate the list
if capitalized do not add to new list
if not capitalized add to newlist
return new list


PATTERNS

init pattern
accumulation pattern
iteration pattern
search and check pattern
