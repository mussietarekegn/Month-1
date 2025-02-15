
class Vehicle:
    def __init__(self, make, model):
        self.__make = make 
        self.__model = model  

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def describe(self):
        return f"This is a {self.__make} {self.__model}."

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def describe(self):
        return f"This car is a {self.get_make()} {self.get_model()} with {self.num_doors} doors."
class Bike(Vehicle):
    def __init__(self, make, model, has_gears):
        super().__init__(make, model)
        self.has_gears = has_gears

    def describe(self):
        gear_info = "with gears" if self.has_gears else "without gears"
        return f"This bike is a {self.get_make()} {self.get_model()} {gear_info}."
def vehicle_info(vehicle):
    print(vehicle.describe())

car = Car("Toyota", "Camry", 4)
bike = Bike("Yamaha", "YZF-R3", True)

vehicle_info(car) 
vehicle_info(bike)  
