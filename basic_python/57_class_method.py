#our problem
'''class Employee:
    company="pogo"
    salary="1000000000000"#class attribute
    location="Siliguri"
    def changeSalary(self ,salary):
        self.salary=salary
e=Employee()
print(e.salary)
e.changeSalary(50)#create an instance attribute
print(e.salary)#object attributes
print(Employee.salary)#class attribute'''

'''even on changing the salary the salary belongs to class didn't get 
affected hence we have to think for classmethods'''

# <Method1> self.__class__.variablename=nameofvariable    called as dunder class
class Employee:
    company="pogo"
    salary="1000000000000"#class attribute
    location="Siliguri"
    def changeSalary(self ,salary):
        self.__class__.salary=salary#it will change the salary belongs class and it will not create any instances
e=Employee()
print(e.salary)
e.changeSalary(50)#create an instance attribute
print(e.salary)#object attributes
print(Employee.salary)#class attribute

print("second method")
# <Method2> self.__class__.variablename=nameofvariable
class Employee:
    company="pogo"
    salary="1000000000000"#class attribute
    location="Siliguri"
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
print(Employee.salary)#class attribute
