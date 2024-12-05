class Vehicle:
    def start_engine(self):
        print('starting engine...')
        
class Car(Vehicle):
    def start_engine(self):
        print('starting car ->')

class Bike(Vehicle):
    def start_engine(self):
        print('starting bike ->')


def test_vehicle(vehicle: Vehicle):
    vehicle.start_engine()

car = Car()
bike = Bike()
test_vehicle(bike)



# understanding LSP -> LISKOV SUBSTITUTE PRINCIPLE

class Main:
    def main_function(self):
        print('from main')

class SubClass(Main):
    def main_function(self):
        print('from sub 1')

class SubClass2(Main):
    def main_function(self):
        print('from sub 2')

sub1 = SubClass()
sub2 = SubClass2()

def implementing(main: Main): #creating object main from Main class
    main.main_function()

implementing(sub2)    
