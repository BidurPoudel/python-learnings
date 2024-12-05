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

    @getModel.setter
    def setModel(self, model):
        self.__model =model

cars = Car("Toyota", "Corolla")

print(cars.__model)
