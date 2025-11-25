import math

class Vector:
    def __init__(self, a, b):
        self.a = a 
        self.b = b 

#__eq__ , __ne__ , __add__ , __sub__ , __neg__ ja __len__
    def __eq__(self, other: 'Vector'):# added more information to defined type of the parameter 
        if not isinstance(other, Vector): # added after teach showed
            return NotImplemented
        return self.a == other.a and self.b == other.b
    
    # def __ne__(self, other):
    #     return self.a != other.a and self.b != other.b
    # ALTERNATIVE WAY TO DO IT MORE ELEGANTLY
    def __ne__(self, other: 'Vector'): # added more information to defined type of the parameter 
        if not isinstance(other, Vector): # added after teach showed
            return NotImplemented
        return not self.__eq__(other)

    def __add__(self, other: 'Vector'):# added more information to defined type of the parameter 
        if not isinstance(other, Vector): # added after teach showed
            return NotImplemented
        return Vector(self.a + other.a, self.b + other.b)

    # def __sub__(self, other: 'Vector'):
    #    if not isinstance(other, Vector): # added after teach showed
    #         return NotImplemented
    #    return Vector(self.a - other.a, self.b - other.b)
    
    def __sub__(self, other: 'Vector'): # more succint solution 
        return self + (-other)
    
    def __neg__(self):
        return Vector(- self.a, - self.b)
    @property
    def lenght(self):
        return math.sqrt(self.a**2 + self.b**2)
    
    def __repr__(self):
        return f"Vector({self.a}, {self.b})"
    def __mul__(self, n: int | float): # added more information to defined type of the parameter 
        if not isinstance(n, (int, float)): # added after teach showed
            return NotImplemented
        return Vector(self.a*n, self.b*n)
    def __rmul__(self, n: int|float):# added more information to defined type of the parameter 
        return Vector(self.a*n, self.b*n)




a = Vector(2, 3)
b = Vector(3, 2)
print(a==b)
print(a!=b)
print(a+b)
print(b+a)
print(a-b)
print(b-a)
print(-a)
print(-b)
print(a.lenght)
print(b.lenght)
print(a*3)
print(3*a)
print(b*5.5)
print(5.5*b)