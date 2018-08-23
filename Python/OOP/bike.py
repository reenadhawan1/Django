class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print(f"Price: {self.price}, Max Speed: {self.max_speed}, Total Miles: {self.miles}")
        return self
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    def reverse(self):
        if self.miles < 5:
            self.miles = 0
            return self
        print("Reversing")
        self.miles -= 5
        return self

bike1 = Bike(290,'30MPH')
bike2 = Bike(210,'21MPH')
bike3 = Bike(250,'25MPH')

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()