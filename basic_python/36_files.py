#variable=open("filename",mode)
#reading file contents using open
#default mode read!!!
#f=open("Sample.txt","r")--reading using read mode specifically mentioned
f=open("Sample.txt")
data=f.read()#reads file data
text=f.read(5)#reads 1st 5 contents of file ,moreover you can't read two times  a file
print(data)
print(text)
f.close()#always close 