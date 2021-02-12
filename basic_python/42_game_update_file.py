def game():
    return 485
new_score=game()
with open("highscore.txt")as f:
    old_score=f.read()
if int(old_score)<new_score or old_score=='':
   with open("highscore.txt","w")as f:
       f.write(str(new_score))
