 elif selection== 2:
        with open('salary_employee.csv', 'w', encoding='utf-8') as ff:
            print(salary_employees)
            ff.write('hello')
            ff.close()
    elif selection== 3:
        with open('salary_employee.csv', 'w', encoding='utf-8') as ff:
            print(salary_employees)
            x = ff.read()
            ff.close()