Toteuta Vector -luokka, joka hyväksyy kaksi lukua alustajassa: Vector(a, b) . Toteuta sille ainakin
__eq__ , __ne__ , __add__ , __sub__ , __neg__ ja __len__ -metodit.
Vector(a, b) == Vector(c, d) =              a == c and b == d
-Vector(a, b) = Vector(-a, -b)

Vector(a, b) + Vector(c, d) = Vector(a+c, b+d)
Vector(a, b) - Vector(c, d) = Vector(a-c, b-d)
len(Vector(a, b)) = sqrt(a**2 + b**2)
Toteuta myös Vectorin skalaaritulo:
Vector(a, b) * n = Vector(a*n, b*n)