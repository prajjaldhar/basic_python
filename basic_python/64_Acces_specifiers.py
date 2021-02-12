# public-to all
# private-sharing with no one
# protected-to specific person
# <Method2> self.__class__.variablename=nameofvariable
class Employee:
    company="pogo"
    salary="1000000000000"#class attribute
    location="Siliguri"
    __private=100
    _protected=50
    def __init__(self,company,salary,location):
        self.company=company
        self.salary=salary
        self.location=location
    @classmethod #decorator
    def changeSalary(cls,salary):#like self cls is used for @classmethod
        cls.salary=salary#it will change the salary belongs class and it will not create any instances
    @classmethod#alternative constructor
    def from_dash(cls,string):
        return cls(*string.split("-"))#on splitting string we are passing varible to class using *args
e=Employee("pogo",180,"siliguri")
print(e.salary)
e.changeSalary(50)#create an instance attribute
print(e.salary)#object attributes
b=Employee.from_dash("Kite-100-matigara")#even on passing a string classmethod makes it different parameters
print(b.salary)
print(b.company)
print(b.location)
#print(b.__private)-->this will not give direct access
#print(b._protected)-->no direct access
print(b._protected)
print(b._Employee__private)#--->by this way you can access private members 
print(Employee.salary)#class attribute
