class person:
    country="United States"
    def __init__(self):#constructor
        print("Initialising person class")
    def takebath(self):
        print(" I take bath even on sundays")
class parents(person):#derived class base class is person
    company="family"
    def __init__(self):
        super().__init__()#base class constructor will going to display
        print("Initialising parent class")
    def getFood(self):
        self.food="burger"
        print(f"Food avaliable is {self.food}")
    def takebath(self):
        print("Luckily I take bath with anti-dandruff shampoo!!!!")
class kids(parents):#derived class base calss is parents
    company="kids_time"
    def __init__(self):
        super().__init__()#base classes of constructors will going to display
        print("Initialising kids class")
    def getFood(self):
        print("all time foods available for kids")
    def takebath(self):
        print("kids don't like to have bath !!!!")
        super().takebath()#printing the method of base class if same name class is present in derived 
p=person()
p.takebath()
e=parents()
e.takebath()
k=kids()
k.takebath()#nearest parent methods will be inherited if there own methods aren't avaliable
'''derived class takes constructor of base class and executes it first before executing any other methods or 
variables'''
print(e.company)
k.getFood()
e.getFood()

 

