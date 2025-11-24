# class Henkilö:
#     def __init__(self, nimi, ikä):
#         self.nimi = nimi
#         self.ikä = ikä


#     def __eq__(self, toinen):
#         return (self.ikä == toinen.ikä and self.nimi == toinen.nimi) or (toinen.ikä == self.ikä and toinen.nimi == self.nimi)
    


# h1 = Henkilö('Matti', 23)
# h2 = Henkilö('Matti', 23)
# h3 = Henkilö('Matti', 24)
# print(h1.__eq__(h2))
# print(h3.__eq__(h1))
# print(h1 == h2) # True
# print(h1 == h3) # False


class mathic:
    def __init__(self, a, b):
        self.a = a 
        self.b = b



    def __add__(self, other):
        return self.a + other.b
    
    def __truediv__(self, other):
        return self.a / other.b
    


a = mathic(2,10)
b = mathic(2, 10)


print(b.__rtruediv__(a))