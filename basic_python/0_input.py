#list comprehension
marks=[int(x) for x in input("ENTER MARKS OF STUDENTS").split(" ")]
print(marks)


#map method
#map(method,variables)
a=list(map(int,input("ENTER MARKS OF STUDENTS").split()))
print (a)
x,y,z=map(int,input("enter values").split())#unpacking of list
print(x+y+z)

#n inputs with multi-line
values=[]#empty list
n=int(input("PLEASE ENTER VALUE OF N"))
for i in range(0,n):
    values.append(int(input()))
print(values)

#n inputs in single line
n=int(input("PLEASE ENTER VALUE OF N"))
a=list(map(int,input("ENTER THE NUMBERS").strip().split()))[:n]
print (a) 