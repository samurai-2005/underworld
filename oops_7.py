class Employee:
    company = "goggle"
    
    def getSalary(self, signature):
        print(f"salary for this employee working in {self.company} is {self.salary}\n {signature}")

    @staticmethod
    def greet():
      print("good morning, sir")

    @staticmethod
    def time():
        print("the time is 9AM in the morning")


harry = Employee()
harry.salary= 100000
harry.getSalary("Thanks!")# Employee.getSalary(harry)
harry.greet() #Employee.greet()
harry.time()