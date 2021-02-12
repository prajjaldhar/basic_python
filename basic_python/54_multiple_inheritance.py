class Employee():#1st base class
    company="google"
    bcode="123"
    def showDetails(self):
        print("This is an Employee Class which is 1st base class")
class Programmer():#2nd base class
    company="jpmorganchase"
    language="python"
    code="548"
    level=0
    def getLanguage(self):
        print(f"The language is {self.language}")
    def upgradeLevel(self):
        self.level=self.level+1
    def showDetails(self):
        print("This is an Employee Class which is 2nd base class")
class Mangement_dept(Employee,Programmer):#passing 2 base classes as an parameter
    language="c++"
    code="88"
    name="prajjal"
    def getLanguage(self):
        print(f"The language is {self.language}")
    def showDetails(self):
        print("This is an Employee Class which is 2nd base class")
e=Employee()
print(e.company)
p=Programmer()
print(p.language)
m=Mangement_dept()
'''this will not going to print jpmorganchase as company because 1st base class is having one company and it is passed
as parameter 1st, so it will going to show google, if you change the passing base classes order then jpmorgan will 
going to displayed'''
print(m.company)
print(m.language)
print(m.name)
print(m.code)
print(m.level)
p.upgradeLevel()#calling base class method using derived class object
print(p.level)
print(m.bcode)