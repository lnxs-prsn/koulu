from book import Book
from member import Member
"""
 library
       -   toggles the states of the book object 
           -   borrowed/ available
       -   toggles the states of he member object using methods of the object itself
           -   can borrow / cannot borrow
       - can only be one library instance


"""

"""
Problems encountered
    -   where are all the books stored to as library is not storage place its coordinator 
    -   I dont know how to connect request from member
        -   so member calls 
    -   I  dont know what I receive from the member
        -   book object or book title 
            -   if I receive the book object dont I break the rule of member class not being able to
            -   directly interact with the book class
"""


class _Library:
    def __init__(self):
        self.library = 'saids library'

    def request_book(self, book: object, member: object) -> bool | str: # I am not sure if this method should manage the borrowing
        if isinstance(book, Book) and isinstance(member, Member):
            if self.can_borrow(member):
                return self.borrow_book(book)
            else:
                return 'borrow limit 10 books you have {member.total_borrowed_books} books'
        else:
            return False
        

    def request_return(self,book: object, member: object) -> bool:
        if isinstance(book, Book) and isinstance(member, Member):
            if self.return_book(book) == True:
                member.borrowed_books.remove(book)
        else:
            return False

    def borrow_book(self, book:object):
        book = book
        return book.borrow()
    
    def return_book(self, book:object):
        book = book
        return book.return_book()
    
    def can_borrow(self, member:object) -> bool:
        return member.can_borrow()


library_instance = _Library()