class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"Fare is Rs.{self.fare}")
        print(f"Seats available {self.seats}")
    def fareInfo(self):
        insurance=2.50*self.fare
        print(f"The Insuarance associated is Rs.{insurance}")
    def bookTicket(self):
        if(self.seats>0):
            print("Booking Successfully Done!!!!")
            print(f"Your seat number is {self.seats}")
            self.seats=self.seats-1
            return self.seats
        else:
            print("Booking failed!!!!!")
            print("Check for tatkal")
if __name__ == "__main__":
    intercity=Train("Kanchanjungha Express: 2450",1200,3)
    intercity.getStatus()
    intercity.bookTicket()
    intercity.fareInfo()
    intercity.getStatus()
    intercity.bookTicket()
    intercity.fareInfo()
    intercity.getStatus()
    intercity.bookTicket()
    intercity.getStatus()
    intercity.bookTicket()