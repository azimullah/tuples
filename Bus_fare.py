class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        maintenance = total_fare * 0.10
        return total_fare + maintenance

bus = Bus(50)
print("Total Bus fare is:", int(bus.fare()))  # Output: 5500
# Output: Total Bus fare is: 5500
# Explanation: The Bus class inherits from Vehicle and overrides the fare method to include a 10% maintenance charge on top of the base fare calculated by the Vehicle  class.
