class Employee:
    company = "google"
    salary = 100

harry = Employee()
rajni = Employee()

#creating instance attribute salary for both the objects
#harry.salary = 300
#rajni.salary = 400
harry.salary = 45
print(harry.salary)
print(rajni.salary)

# below line throws an error as address is not present in instance/class
#print(rajni.address)