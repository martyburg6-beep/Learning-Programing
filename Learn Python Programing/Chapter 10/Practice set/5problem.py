
from random import randint


class train:
    def __init__(self,trainno):
        self.trainno=trainno
    def book(self,fro,to):
        print(f"ticket is booked for train no: {self.trainno} from {fro} to {to}")
    def getstatus(self):
        print(f"train no:{self.trainno}is running on time")
    def getfare(self,fro,to):
        print(f"ticket fare in train no: {self.trainno} from {fro} to {to} is {randint(22,555)}")

t =train(12329)
t.book("islamabad","karachi")
t.getstatus()
t.getfare("islamabad","karachi")