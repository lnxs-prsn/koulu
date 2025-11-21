class Car():
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed
        self.info = f'{brand} \nColor:{color} \nSpeed:{speed} \n'

audi = Car('Audi', 'Red', 200)

print(audi.info)