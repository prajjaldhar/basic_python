words=["subscribe this","click on this","makey money","buy this","swipe up"]
text=input("ENTER A TEXT\n")
flag=0
text=text.lower()
for spam in words:
    if spam in text:
        flag+=1
    else:
        pass
if flag>0:
    print("It's a Spam")
else:
    print("Not Spam")