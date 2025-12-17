import library

"""
   -   book
       -   stores data related to book and its states
       -   has method borrow which changes the state
       -   has method to return which changes the state
       -   has attribute available boolean

"""

"""
problems found in the design 
    - if there is multiple books of same title how do I know which am borrowing or which am returning
"""
class Book:
    def __init__(self, title: str, author:str, content:str) -> None:
        self.title = title
        self.author = author
        self.content = content
        self.available = True
    # borrow the book
    def borrow(self) -> bool | str:
        if self.available:
            self.available = False
            return self.available
        else:
            return 'book is not available'
        
    # return the book
    def return_book(self) -> str:
        if self.available == False:
            self.available = True
            return self.available
        else:
            return 'book is aready in the library'