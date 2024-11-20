from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in trainNo {self.trainNo}  from {fro} to to {to}")
    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time")
    def getFare(self,fro,to):
        print(f"Ticket fare in trainNo {self.trainNo} from {fro} to {to} is {randint(500,2000)}")

t=Train(332231)
t.book("Dhaka","Chattogram")
t.getStatus()
t.getFare("Dhaka","Chattogram")                
              