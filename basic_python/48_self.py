''' self refers to the instance of the class 
    it automatically refers to the function call from an object'''
class Employee:
    company="Google"
    def getSalary(self):
        print(f"salary is {self.salary} working in {self.company}")
prajjal=Employee()#object is created
prajjal.salary=10000#instance attribute
prajjal.getSalary()#prajjal here is an object
#Employee.getSalary(prajjal) #this is the actual statement,where object is passed as parameter
'''classname.class_function(object)'''
