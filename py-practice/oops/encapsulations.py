


# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
    
#     def getBrand(self):
#         return self._brand
    
#     def setBrand(self, brand):
#         self.__brand = brand


# cars = Car("Toyota", "Corolla")

# cars.__brand = "farari"

# print(cars.__brand)

# ----------------------- getter and setter method in another way----------------------------


class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    
    # getter method
    @property
    def getModel(self):
        return self.__model
    
    # setter method
    @getModel.setter
    def setModel(self, model):
        self.__model =model

cars = Car("Toyota", "Corolla")

# print(cars.__model)



class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.__age = None
        self.set_age(age)
        self.__address = address

    def get_age(self):
        return self.__age
    
    def set_age(self,value):
        if value>18:
            self.__age = value
        else:
            raise ValueError("Age must be greater than 18.")

# Test
try:
    person = Person("bidur", 12, 'lakeside')  # This will now raise an error
    print(person.get_age())
except ValueError as e:
    print(e)  # Output the error message
