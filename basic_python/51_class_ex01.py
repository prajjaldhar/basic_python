class Programmer:
    company="IBM"
    def __init__(self,name,product,company):
        self.name=name
        self.product=product
        self.company=company
    def getInfo(self):
        print(f"The name of the company is {self.company}")
        print(f"The name of the programmer is {self.name}")
        print(f"Product is {self.product}")
prajjal=Programmer("Prajjal","Github","json")
rohan=Programmer("Rohan","skype","Microsoft")
prajjal.getInfo()
rohan.getInfo()