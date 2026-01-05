class Employee:
    def __init__(self, id):
        self.name = self.ask_name() 
        self.id = id

    def ask_name(self):
        try:
            self.name = str(input("Please enter employee name:"))
        except:
            self.name = ''
        return self.name


class SalaryEmployee(Employee):
    def __init__(self, id, salary):
        super().__init__(id)
        self.id
        self.salary = self.ask_salary()
        self.type = 'M'


    def ask_salary(self):
        try:
            self.salary = int(input("Please enter monthly salary:"))
        except:
            self.salary = 0
        return self.salary

    def calculate_salary(self):
        return self.salary


class HourlyEmployee(Employee):
    def __init__(self, id):
        super().__init__(id)
        self.hour_rate = self.ask_hour_rate()
        self.hours_worked = self.ask_hours_worked()
        self.type = 'H'

    def ask_hour_rate(self):
        try:
            self.hour_rate = int(input("Please enter hour rate:"))
        except:
            self.hour_rate = 0
        return self.hour_rate

    def ask_hours_worked(self):
        try:
            self.hours_worked = int(input("Please enter hours worked:"))
        except:
            self.hours_worked = 0
        return self.hours_worked
    def calculate_salary(self):
        return self.hour_rate*self.hours_worked
    



class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, salary):
        super().__init__(id, salary)
        self.commission = self.ask_commission()
        self.type = 'C'

    def ask_commission(self):
        try:
            self.commission = int(input("Please enter commission:"))
        except:
            self.commission = 0
        return self.commission

    def calculate_salary(self):
        return self.commission+self.salary
    

com = CommissionEmployee(10, 0)
print(com.calculate_salary())
