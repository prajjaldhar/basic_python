li=[58,1,2,3,6,5,4]
print(li)
print(li[5])
li[3]=15#acessing using indexing
print(li)
li.append(59)#appending(adds at last)
print(li)
li.insert(8,90)#inserts 90 at 8th index
print(li)
#poping
li.pop(6)#removes from particular indes
print(li)
#removes
li.remove(90)#pops particular element
print(li)
print(li[::-1])#reversing

#list slicing
friends=["rohan","shubham","suraj","aditya"]
print(friends[::-1])

#list sort
li.sort()#list sorted
print(li)
#reverse
li.reverse()
print(li)