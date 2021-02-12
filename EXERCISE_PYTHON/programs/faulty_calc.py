#produce wrong o/p for calculation of 45*3=555,56+9=77,56/6=4,235-99=100
while(1):
    print("to exit type b else c")
    c=input("Enter Choice ")
    if c=="c":
        a=int(input("ENTER VALUE OF 1ST OPERAND "))
        b=int(input("ENTER VALUE OF 2ND OPERAND "))
        operator=input("ENTER OPERATOR SIGN ")
        if operator=="+":
            if(a==56 and b==9)or(a==9 and b==56):
                print("77")
            else:
                print(a+b)
        if operator=="-":
            if(a==235 and b==99)or(a==99 and b==235):
                print("100")
            else:
                print(a-b)
        if operator=="*":
            if(a==45 and b==3)or(a==3 and b==45):
                print("555")
            else:
                print(a*b)
        if operator=="/":
            if(a==56 and b==4):
                print("4")
            else:
                print(a/b)
    else:
        exit()