class Employee:
    company = "google"
    salary = 100

harry = Employee()
rajni = Employee()
harry.salary = 300
rajni.salary = 400

print(harry.company)
print(rajni.company)
Employee.company ="youtube"
print(harry.company)
print(harry.salary)
print(rajni.company)
print(rajni.salary)