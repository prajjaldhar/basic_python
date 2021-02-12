class Employee:
    salary=10000000#static
    increment=1.5#variable
    @property
    def totalSalary(self):
        return self.salary*self.increment
    @totalSalary.setter
    def totalSalary(self,val):
        self.increment=float(val/self.salary)
e=Employee()
print(e.totalSalary)
e.totalSalary=2000000
print(e.salary)
print(e.increment)