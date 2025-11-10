class Employee:
    id_counter = 0
    def __init__(self,name):
        Employee.id_counter += 1
        self.id = Employee.id_counter
        self.name = name 
        def calculate_salary(self):
            pass # child implements 


class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
    



class PayRollSystem():

    def calculate_payroll(self, employeelist):
        for employee in employeelist:
            print('Employee Payroll')
            print('================')
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_salary()}')
            print()
        
        

employeelist = []
while True:
    name = input('Please enter employee name (0 to quit):')
    if name == '0':
        break
    salary = int(input('Please enter salary:'))

    employee = SalaryEmployee(name, salary)
    employeelist.append(employee)

pay = PayRollSystem()
pay.calculate_payroll(employeelist)

"""
Over all well done 
for the future include comments while coding 
as that is the best way to instill the habit
"""