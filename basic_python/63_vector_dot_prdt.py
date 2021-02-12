class Vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        str1 = ""
        index=0
        for i in self.vec:
            str1+=f"{i}a{index} + "
            index+=1
        return str1[:-2]
    def __add__(self,vec2):
        newlist=[]
        for i in range(len(self.vec)):
            newlist.append(self.vec[i]+vec2.vec[i])
        return Vector(newlist)
    def __mul__(self,vec2):
        add=0
        for i in range(len(self.vec)):
            add+=(self.vec[i]*vec2.vec[i])
        return add
v1=Vector([1,5,7,8,45,8,9,2,66,100])
v2=Vector([4,8,9,88,22,44,33,22,13,49])
add=v1+v2
print(add)
mul=v1*v2
print(mul)