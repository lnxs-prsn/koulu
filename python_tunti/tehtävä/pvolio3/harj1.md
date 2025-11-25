mika = Person('Mika', 'Suomalainen')
print(mika) # <Person Mika Suomalainen>

seppo = Student('Seppo', 'Suomalainen')
print(f'{seppo} - Email: {seppo.email}') # <Student Seppo Suomalainen (1)> - Email:
ss000001@edu.taitotalo.fi

chrisu = Teacher('Christian', 'Finnberg', 'Python')
print(f'{chrisu} - Email: {chrisu.email}') # <Teacher Christian Finnberg> - Email:
christian.finnberg@taitotalo.fi

teijo = Student('Teijo', 'Tehokas')
print(f'{teijo} - Email: {teijo.email}') # <Student Teijo Tehokas (2)> - Email:
tt000002@edu.taitotalo.fi