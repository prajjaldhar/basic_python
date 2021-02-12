with open("another.txt","r")as f:
    data=f.read()
    flag=0
    word=input("ENTER THE WORD TO BE SEARCHED INSIDE FILE\n")
    if word in data.lower():
        flag=flag+1
if flag>0:
    print(f"{word} is found")
else:
    print(f"{word} is not found")