class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):# this method takes two arguments self and second variable passed named as num2 here
        print("adding")
        return Number(self.num+num2.num)
    def __mul__(self,num2):# this method takes two arguments self and second variable passed named as num2 here
        print("multiplying")
        return Number(self.num*num2.num)
    def __str__(self):
        return f"decimal number:{self.num}"
    def __len__(self):
        return 1
n1=Number(4)#here n1 is an Number object not an integer
n2=Number(5)#n2 is also an Number object
n3=Number(3)
add=n1+n2
mul=n1*n2*n3
print(add)
print(n2)
print(mul)
print(len(n1))
'''more suvh operators are '''
# p1+p2 --->p1__add__(p2)
# p1-p2--->p1__sub__(p2)
# p1*p2---->p1__mul__(p2)
# p1/p2---->p1__div__(p2)
# p1//p2---->p1__floordiv__(p2)
