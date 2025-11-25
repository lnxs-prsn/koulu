class Point:
def __init__(self, param1, param2=None) -> None:
pass
p1 = Point(4, 5) # Kaksi parametria: int 4 ja int 5
print(p1.x) # 4
print(p1.y) # 5
p2 = Point((7, 8)) # Yksi parametri: tupla (7, 8)
print(p2.x) # 7
print(p2.y) # 8