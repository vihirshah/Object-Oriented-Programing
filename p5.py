class vehicle():

    def __init__(self,milege,cost):
        self.milege=milege
        self.cost=cost

    def show_details(self):
        print("milege of vehicle --> ",self.milege)
        print("cost --> ", self.cost)

class car(vehicle):
    
    def show_car(self):
        print("i am a car")

c1=car(200,200000)
c1.show_details()
c1.show_car()