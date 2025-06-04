class Employee:
    company = "goggle"

    def __init__(self, name, salary, subunit):
       self.name= name
       self.salary = salary
       self.subunit = subunit
       print("Employee is created!")

    def getdetails(self):
       print(f"The name of the employee is {self.name}")
       print(f"The salary of the employee is {self.salary}")
       print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self, signature):
        print(f"salary for this employee working in {self.company} is {self.salary}\n {signature}")

    @staticmethod
    def greet():
      print("good morning, sir")

    @staticmethod
    def time():
        print("the time is 9AM in the morning")

harry = Employee("harry", 100, "youtube")
#harry = Employee() --> This throws an error missing 3 required positional arguments:)
harry.getdetails()
