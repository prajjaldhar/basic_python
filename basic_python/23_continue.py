for i in range(0,10):
    if (i%2)==0:
      continue#skips that value of i mentioned in conditional syntax
    if i==5:
        continue
    print(i)
else:
    print("this is inside for loop ladder")#this shows that for loops ends naturally not abruptly 