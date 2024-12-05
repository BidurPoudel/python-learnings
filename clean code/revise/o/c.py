class Vehicle:
    def start_engine(self):
        pass
            
class Bike(Vehicle):
    def start_engine(self):
        print("Bike is starting")
    def cost(self, price: int):
        return f"{price: 200}"

class Car(Vehicle):
    def start_engine(self):
        print("From car class -> Car is starting")
        


class Type(Vehicle):
    def vehicle_type( self,vehicle: Vehicle):
         vehicle.start_engine()

bike = Bike()
car = Car()
car.start_engine()

type = Type()
type.vehicle_type(car)
type.vehicle_type(bike)