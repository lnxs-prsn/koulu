import time

class Person:
    def __init__(self, first_name: str, last_name:str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    # def __rper__(self) -> str:
    #     return f'{self.first_name} {self.last_name}'
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Student(Person):
    id = 0
    def __init__(self, first_name, last_name) -> None:
        Student.id += 1
        super().__init__(first_name, last_name)
        self.email = f'{self.first_name[0].lower()}{self.last_name[0].lower()}{Student.id:06}@taitotalo.fi'






    def __str__(self) -> str:
        return f'<{self.first_name} {self.last_name} ({Student.id})> - Email: {self.email}'
class Teacher(Person):
    id = 0
    def __init__(self, first_name, last_name, course) -> None:
        super().__init__(first_name, last_name)
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@taitotalo.fi'
        self.course = course
        Teacher.id += 1
    def __str__(self) -> str:
        return f'<Teacher: {self.first_name} {self.last_name}> - Email: {self.email}'






mika = Person('Mika', 'Suomalainen')
print(mika) # <Person Mika Suomalainen>

seppo = Student('Seppo', 'Suomalainen')
print(f'{seppo} - Email: {seppo.email}') 

chrisu = Teacher('Christian', 'Finnberg', 'Python')
print(f'{chrisu} - Email: {chrisu.email}')

teijo = Student('Teijo', 'Tehokas')
print(f'{teijo} - Email: {teijo.email}') 





