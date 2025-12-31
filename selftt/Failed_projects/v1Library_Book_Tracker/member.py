from library import library_instance

"""
 member 
       -   stores states and user data
       -   has method  request book for borrowing from library
       -   has method request_return for returning to library
       -   has state can_borrow boolean  returns boolean
       -   has int variable total_books borrowed
       -   has list of books borrowed so far 

"""

"""
problems I have encountered 
    -   I have system level design but no object level design 
        -   is there a way the system level design would lock in certain object level designs ?
        -   so I could lower the amount of decision I have to make per object.

"""

class Member:
    
    def __init__(self, name:str, address: str) -> None:
        self.name = name
        self.address = address
        self.borrowed_books = []
        self.total_borrowed_books = len(self.borrowed_books)
        self.can_borrow_ = True
    
    def request_borrow(self, book: object) -> str:
        library = library_instance
        if library:
            library.request_book(book, self)
            return 'request pending'
        else:
            return '{library} does not exist'
        
    def request_return(self, book:object):
        library = library_instance
        if library:
            return library.request_return(book, self)#:
#                self.borrowed_books.remove(book)      issue here is that member cannot take action 
# it can only  request and the library is the action taker 
# all actions happen in one place and they all get edited in one place
    def can_borrow(self):
        if self.total_borrowed_books >=10:
            self.can_borrow_ = False
        else:
            self.can_borrow_ = True