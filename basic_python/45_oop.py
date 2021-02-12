#do not repeat yourself(dry principles)
#a=12
#b=34
#print(a+b) procedural oriented programming
#oop programming
#class is blueprint
#it has  no instances
#class is  basically written in pascal case 
'''PascalCase it has begining letter in capital and middle word in capital eg.EmployNumber'''
''' camelCase it has begining letter in small and middle in capital eg. isFloat'''
#onject instanciation allocates memory
class num:
    def sum(self):
        return self.a+self.b
number=num()#creating object
num.a=12
num.b=32
s=number.sum()
print(s)
#modelling of oops

''' name--->class--->employee
    adjective--->attributes--->name,age,salary,gender
    verbs---->methods(functions)---->getsal(),increament(),printdata() 
    for whole lot of bunch'''
'''class attributes
   an attributes that belongs to the class rather than a particular object
   class Employee:
       company="google"
       salary=200
   prajjal=employee()
   suraj=employee()
   print(prajjal.company)
   print(suraj.company)
   employee.company="Firefox"---->class attributes
   print(prajjal.company)'''
# to change the attributes for object like their personal details comes under object attributes although they belong to same class
'''prajjal.salary=300
   suraj.salary=400''' #this is insatance attributes