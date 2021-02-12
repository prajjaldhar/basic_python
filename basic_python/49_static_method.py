'''@staticmethod converts classname.function(no arguments)
    if @staticmethod is not present than it always shows classname.function(object as argument)
    it is a decorator a special function'''
class Employee:
    company="Google"
    def getSalary(self):
        print(f"salary is {self.salary} working in {self.company}")
    @staticmethod
    def greet():
        print("hello sir!!!!!")
    def getage(self):
        print(f"age is {self.age}")
prajjal=Employee()#object is created
prajjal.salary=10000#instance attribute
prajjal.getSalary()#prajjal here is an object
#Employee.getSalary(prajjal) #this is the actual statement,where object is passed as parameter
prajjal.greet()#Employee.greet()
prajjal.age=12#instance attribute
prajjal.getage()

