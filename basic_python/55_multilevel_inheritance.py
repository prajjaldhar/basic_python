class person:
    country="United States"
    def takebath(self):
        print(" I take bath even on sundays")
class parents(person):#derived class base class is person
    company="family"
    def getFood(self):
        self.food="burger"
        print(f"Food avaliable is {self.food}")
    def takebath(self):
        print("Luckily I take bath with anti-dandruff shampoo!!!!")
class kids(parents):#derived class base calss is parents
    company="kids_time"
    def getFood(self):
        print("all time foods available for kids")
p=person()
p.takebath()
e=parents()
e.takebath()
k=kids()
k.takebath()#nearest parent methods will be inherited if there own methods aren't avaliable
print(e.company)
k.getFood()
e.getFood()

 

