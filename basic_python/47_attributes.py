class employee:
       company="google"
       salary=200
prajjal=employee()#creating object1
suraj=employee()#object2
print(prajjal.company)
print(suraj.company)
employee.company="Firefox"#---->class attributes
print(prajjal.company)#value of company gets changed using class attribute see above
prajjal.salary=300#object attributes
suraj.salary=400 #this is insatance attributes
print(suraj.salary)
print(prajjal.salary)
''' if neither class attribute nor instanec attribute is present than it will show error and
  if only one of them is present than it will give prefer to object than class
  if only class attribute is present than only class attribute will going to display
 '''