# [[1,2,3],
# [4,5,6],
# [7,8,9]]
def matrix(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range(n):
            inp=int(input(f"ENTER O[{i}][{j}]"))
            row.append(inp)#appending each column
        o.append(row)#now appending each coloumn in each row
    return o #returning list of list
def MatrixSum(A,B):
    o=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j]+B[i][j])
        o.append(row)
    return o
n=int(input("ENTER THE VALUE FOR N\n"))
m=int(input("ENTER THE VALUE FOR M\n"))
print("ENTER MATRIX A")
A=matrix(m,n)
print(A)
print("ENTER MATRIX B")
B=matrix(m,n)
print(B)
s=MatrixSum(A,B)
print(s)
