#Inheriting properties from base class
#single level inheritance
class Employee:
    company="google"
    def showDetails(self):
        print("This is an Employee Class")
class Programmer(Employee):#passing base class as an parameter
    language="python"
    def getLanguage(self):
        print(f"The language is {self.language}")
e=Employee()
e.showDetails()
p=Programmer()
p.showDetails()#this will inherits details from base class
p.getLanguage()#this will display from it's own class
print(p.company)#this company details are inherited from base class if no such variable or methods available in derived class

