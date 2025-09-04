from employee import Employee

from database import create_table

def main():
    create_table()

    while True:
        print("\n===========Employes Managment System===========")
        print("1. Add Employee")
        print("2. Viwe All Enployee")
        print("3. Exit")

        choice=input("Enter choice..")

        if choice=="1":
            name=input('Enter your name:')
            age=input('Enter your age:')
            dep=input('Enter your Department:')
            salary=float(input('Enter your Salary:'))

            emp = Employee(name,age,dep,salary)
            emp.save()

        elif choice=="2":
            employees=Employee.get_all()
            print("\n ----Employee List----")
            for emp in employees:
                print(emp)


        elif choice=="3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again!")

if __name__=="__main__":
    main()

