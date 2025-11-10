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
                        -   method takes an employeelist
                -   EMPLOYEE HAS ATTRIBUTES:
                    -   id, name
                -   EMPLOYEE HAS METHODS:
                    -   calculate_salary # is implemented by the child classes
                -   SALARYEMPLOYEE HAS ATTRIBUTES: # INHERITS id,name FROM EMPLOYEE
                    -   monthly_salary
                -   SALARYEMPLOYEE HAS METHODS:
                    -   calculate_salary # implements parent method
                    -   



 Phase 2: DESIGN & STRUGGLE
- Design solution (how will it work?)
- Find mistakes early (what could go wrong?)
  - the task has strict naming convention if I dont use similar naming it wont work
  - for id to perisist I have to define it outside of the constructor 



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


essentially this happens 

employee creates employees 
salaryemployee inherits and adds its own attribut 
and uses method of employee to calculate salary 

payrollsystem takes list of instances from the salaryemployee
has method calculate_payroll which calls calculate_salary of every employee in the list



problem:
    -   the payrollsystem prints only one employee 
        -   if return is inside an loop it breaks out of the loop 
    -   it printed None 
        -   reason if function is called inside and print() and has no explicit return of value it will print also None
        -   solution is call method() without print()
        -   if method is inside an class it has by default self included by the syntax even if the user forgets to add it and it that case 
            -   error occurs:
                -   pay.calculate_payroll(employeelist)
                -   TypeError: PayRollSystem.calculate_payroll() takes 1 positional argument but 2 were given

ALHAMDULILLAAH IT WORKED

the blueprint works for the purpose of achieving organized problem solving 
    -   the real issue is the user impulse to solve without thinking and just feeling is immense
    -   I need multiple small doable task to instill habit 
        -   what I learned is if task is too easy then using the blueprint becomes very chanllenging as most of the effort goes explaining to oneself 
        -   why so much effort something so easy.