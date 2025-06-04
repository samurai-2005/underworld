class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"name is {self.name}")
        print(f"train is {self.train}")

aaravApplication = RailwayForm()
aaravApplication.name = "Aarav"
aaravApplication.train = "Garibrath Express"        
aaravApplication.printData()