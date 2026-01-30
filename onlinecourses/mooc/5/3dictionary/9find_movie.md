
Please write a function named find_movies(database: list, search_term: str), which processes the movie database created in the previous exercise. The function should formulate a new list, which contains only the movies whose title includes the word searched for. Capitalisation is irrelevant here. A search for ana should return a list containing both Anaconda and Management.
An example of its use:
database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
{"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
{"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]
my_movies = find_movies(database, "python")
print(my_movies)
Sample output
[{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]
LOGICAL OPERATIONS
   -   find_movies(db: list, search_term:str)
       -   found_movies = [db[x], if ]
1. yes
   1. 2 for loops
   2. if statement
2. yes
   1. second for loop happens after first loop
   2. if statement happens after the second loop
3. yes
   1. if startswith
   2. then append
4. yes
   1. loop gets new index number from the for loop
5. yes
6. yes
   1. match word to movies
7. yes
   1. access storage
   2. search and match
   3. append to new storage if match