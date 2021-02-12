def percentage(marks):
    return sum(marks)/len(marks)

marks=[int(x) for x in input("ENTER MARKS OF STUDENTS").split(" ")]
print(percentage(marks))

#sum using function
def mysum(num1,num2):
    """this is doc string"""
    return num1+num2
num1=int(input("enter value of num1: "))
num2=int(input("enter value of num2: "))
print(mysum(num1,num2))
print(mysum.__doc__)#prints the doc string