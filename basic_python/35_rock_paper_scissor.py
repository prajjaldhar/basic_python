import random
def Game(comp,you):
    if comp=="R":
        if you=="S":
            return False
        if you=="P":
            return True
    if comp=="S":
        if you=="P":
            return False
        if you=="R":
            return True
    if comp=="P":
        if you=="R":
            return False
        if you=="S":
            return True
if __name__ == "__main__":
    print("Comp Turn: Rock(R) Paper(P) or Scissor(S)?")
    randno=random.randint(1,3)#generates random number
    if(randno==1):
        comp="R"
    elif(randno==2):
        comp="P"
    elif(randno==3):
        comp="S"
    you=input("Your Turn: Rock(R) Paper(P) or Scissor(S)? ")
    win=Game(comp,you)
    print(f"Computer chose {comp} ")
    print(f"You chose {you} ")
    if win==None:
        print("TIE!!!!!")
    elif win:
        print("YOU WIN!!!!!!")
    else:
        print("COMP WINS!!!!!!")