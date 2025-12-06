Exercise: SalaryEmployee to CSV-file
Max score: 1
In this exercise you will write and read your class SalaryEmployee to and from a file salary_employee.csv in format of comma separates values . You must use your own my_join and my_split functions. 

Program menu as below:

(1) Add employee to employees 
(2) Write employees to file 
(3) Read employees from file 
(4) Print employees 
(0) Quit

With menu option 1 you will read employee names and their salary to objects.
With menu option 2 you will write all objects to csv-file.
With menu option 3 you will read objects from csv-file.
With menu option 4 you will print objects and their values in a format like: Id: 1 Name: Jane Doe Salary: 5555.

With menu option 0 you will quit the execution of program.

Your job is to code for menu options 2 and 3.

Write employees to file:

make sure that file salary_employee.csv is empty,
go thru salary employees, add its attributes to a list and use my_join to make csv-string from that list,
complete string with newline and write it to file,
when all employees are handled, remember to close the filehandle,
add the following code to the end: print(len(salary_employees) ," employee(s) added to salary_employee.csv").
Read employees from file:

open file salary_employee.csv for reading,
go thru the file line by line,
strip newline and use my_split to make attribute list from string,
make SalaryEmployee object and add it to salary_employees list,
close file when all lines are read,
add following code to the end: print(len(salary_employees) ," employee(s) read from salary_employee.csv").
Example output:
(1) Add employee to employees
(2) Write employees to file
(3) Read employees from file
(4) Print employees
(0) Quit

Please select one: 1
Please enter employee name (0 to quit):Jane Doe
Please enter salary:5555
Please enter employee name (0 to quit):John Johnson
Please enter salary:4567
Please enter employee name (0 to quit):Richard Roe
Please enter salary:3636
Please enter employee name (0 to quit):0
(1) Add employee to employees
(2) Write employees to file
(3) Read employees from file
(4) Print employees
(0) Quit

Please select one: 2
3  employee(s) added to salary_employee.csv
(1) Add employee to employees
(2) Write employees to file
(3) Read employees from file
(4) Print employees
(0) Quit

Please select one: 4
Id: 1 Name: Jane Doe Salary: 5555
Id: 2 Name: John Johnson Salary: 4567
Id: 3 Name: Richard Roe Salary: 3636
(1) Add employee to employees
(2) Write employees to file
(3) Read employees from file
(4) Print employees
(0) Quit

Please select one: 3
3  employee(s) read from salary_employee.csv
(1) Add employee to employees
(2) Write employees to file
(3) Read employees from file
(4) Print employees
(0) Quit

Please select one: 4
Id: 1 Name: Jane Doe Salary: 5555
Id: 2 Name: John Johnson Salary: 4567
Id: 3 Name: Richard Roe Salary: 3636
(1) Add employee to employees
(2) Write employees to file
(3) Read employees from file
(4) Print employees
(0) Quit

Please select one: 0
Service shutting down, thank you.
The output of the program must be exactly the same as the example output (the most strict comparison level)

