class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if self.big >= 1 and carType == 1:
            self.big -= 1
            return True
        elif self.medium >= 1 and carType == 2:
            self.medium -= 1
            return True
        elif self.small >= 1 and carType == 3:
            self.small -= 1
            return True
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)