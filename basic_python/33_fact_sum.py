# 1!+2!+3!+.....+n!
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return fact(n-1)*n
def sum(n):
    sum=0
    i=1
    while i<=n:
        sum=sum+fact(i)
        i=i+1
    return sum
n=int(input("Enter value of n: "))
print(sum(n))