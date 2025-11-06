Deep Practice Template (Simplified)

Define first classes

PayrollSystem, having method calculate_payroll and getting a list of employees as a parameter. Method should calculate and print payroll for employees.
SalaryEmployee, a subclass of Employee. SalaryEmployee has its own attribute monthly_salary and method calculate_salary, which will return the monthly salary of an employee.
Finally make then program,

asking employee name as in previous Employee-exercise and also asking monthly salary for SalaryEmployee-class.
creating SalaryEmployee-objects and store them into a list.
ending when user gives '0' instead of a name. 
using at the end PayrollSystem to print Payroll for Employees in a format shown in the example below.
 Phase 1: CHUNK IT
- Understand the problem (what are we building?)
- Break into pieces (what are the smallest learnable parts?)

    -   WE ARE BUILDING PAYROLLSYSTEM
        -   it has classess:
            -   PAYROLLSYSTEM, EMPLOYEE,SALARYEMPLOYEE
                -   PAYROLLSYSTEM HAS ATTRIBUTES:
                    -   NO ATTRIBUTES
                -   PAYROLLSYSTEM HAS METHODS:
                    -   calculate_payroll
                -   EMPLOYEE HAS ATTRIBUTES:
                    -   id, name
                -   EMPLOYEE HAS METHODS:
                    -   calculate_pay # is implemented by the child classes
                -   SALARYEMPLOYEE HAS ATTRIBUTES: # INHERITS id,name FROM EMPLOYEE
                    -   monthly_salary
                -   SALARYEMPLOYEE HAS METHODS:
                    -   calculate_pay # implements parent method
                    -   



 Phase 2: DESIGN & STRUGGLE
- Design solution (how will it work?)
- Find mistakes early (what could go wrong?)
- Correct mentally (fix the design before coding)

 Phase 3: LEARN FROM OTHERS
- Research 15 min: Find 2-3 examples online
- Note patterns: What do good developers do?
- Avoid anti-patterns: What do bad examples do?

 Phase 4: IMPLEMENT
- Code with focus
- Embrace errors (they're learning moments)
- Fix and repeat (build better neural pathways)

That's it. Four clean phases. No complexity.



essentially this happens 

employee creates employees 
salaryemployee inherits and adds its own attribut 
and uses method of employee to calculate salary 

payrollsystem takes list of instances from the salaryemployee
has method calculate_payroll which calls calculate_salary of every employee in the list
