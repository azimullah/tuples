from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass

    @abstractmethod
    def max_speed(self):
        pass


class BMW (vehicle):
    def fuel_type(self):
        print("BMW runs on petrol")

    def max_speed(self):
        print("BMW max speed is 250 km/h")

class ferrarie (vehicle):
    def fuel_type(self):
        print("ferrarie runs on deisel")

    def max_speed(self):
        print("ferrarie max speed is 290 km/h")
    
q=BMW()
q.fuel_type()
q.max_speed()

lp= ferrarie()
lp.fuel_type()  
lp.max_speed()