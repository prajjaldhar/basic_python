class Employee:
    company="pogo"
    salary=12 #class attribute and it has fixed value
    salarybonous=8 #variable value
    #totalSalary=6100 hard cored value
    @property #decorator this is called getter
    def totalSalary(self):#totalSalary is not a function it's a property
        return self.salary+self.salarybonous #it will change the salary belongs class and it will not create any instances
    @totalSalary.setter #setter decorator @function_name.setter
    def totalSalary(self,val):
        self.salarybonous=val-self.salary
e=Employee()
print(e.totalSalary)
e.totalSalary=100
print(e.salary)
print(e.salarybonous)

