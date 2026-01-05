class PayrollSystem():
    def calculate_payroll(self, employees):
        for employee in self.employees:
            print('Employee Payroll')
            print('================')
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_salary()}')
            print('')
            