seta={1,2,3,4}
print(seta)
setb={1,1,2,3,4,4,4,5,6}#removes the duplicates always prints unique values
print(setb)
print(type(setb))
#IMPORTANT:
a={}
print(a)#its a empty dictionary not an empty set
print(type(a))
#an empty set can be created using below syntax
b=set()
print(b)
print(type(b))
#list acnnot be added inside set
#b.add([4,5,6]) unhashable
#b.add({1:5}) dictionary also can't also cannot be added
#print(b)

#adding and removing
b.add(5)
b.add(15)
b.add(25)
print(len(b))
b.remove(15)
print(b)

#poping
b.pop()
print(b)