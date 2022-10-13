def show_employee(name='anonymous',salary='9000'):
    print(f"Employe Name : {name} Salary : {salary}")

name = input("Enter Employe Name : ")
salary = input("Enter Salary : ")

show_employee(name,salary)
show_employee()
