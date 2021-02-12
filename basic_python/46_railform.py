class RailwayForm:
    formType="RailwayForm"
    #default arguments
    name="Rahul"
    train="Chennai Express"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
application=RailwayForm()
application.name="prajjal"
application.train="Rajdhani Express"
application.printData()