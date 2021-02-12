a="string is happy"
print(a[0:])
print(a[2:9])
print(a[-7:-1])
print(a[::-1])
i=int(input("enter the index to be searched"))
if i>len(a):
    print("Out of index")
else:
    print(a[i])