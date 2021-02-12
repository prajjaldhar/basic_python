f=open("Sample.txt")
#reads 1st line
data=f.readline()
print(data,end=" ")
#reads 2nd line
data=f.readline()
print(data,end=" ")
#reads 3rd line
data=f.readline()
print(data,end=" ")
f.close()#always close 

#r=opens for reading
#w=opens for writing
#a=opens for appending
#+=opens for updating
#rb=opens in binary for reading
#wb=opens in binary for reading