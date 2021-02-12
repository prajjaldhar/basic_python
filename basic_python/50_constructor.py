''' __init__() constructor is a speacial method/function which is first run when an object is created
takes self and other arguments '''
class Employee:
    company="Google"
    def __init__(self,name,salary,unit):#constructor
        print("Object is created")
        #default types passed
        self.salary=salary
        self.name=name
        self.unit=unit
        self.age=18
    def getDetails(self):
        print(f"The Name of the Employee is {self.name}")
        print(f"The salary of the Employee is {self.salary}")
        print(f"The unit of the Employee is {self.unit}")
    @staticmethod
    def greet():
        print("hello sir!!!!!")
    def getage(self):
        print(f"age is {self.age}")
prajjal=Employee("prajjal","100","ece")#object is created
prajjal.getDetails()
prajjal.getage()
