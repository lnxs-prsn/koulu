class Employee:
    def __init__(self, id, name):
        self.id = id 
        self.name = name 
        def calculate_pay(self):
            pass # child implements 


class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary
        def calculate_pay(self, monthly_salary):
            return monthly_salary
        




class PayRollSystem(SalaryEmployee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name, monthly_salary)