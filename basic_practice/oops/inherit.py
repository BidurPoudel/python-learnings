class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def getName(self):
        return self.__name
    
    @getName.setter
    def setName(self, name):
        self.__name = name
    

    @property
    def getAge(self):
        return self.__age
    

    @getAge.setter
    def setAge(self, age):
        self.__age = age


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.__breed = breed


    @property
    def getBreed(self):
        return self.__breed
    
    @getBreed.setter
    def setBreed(self, breed):
        self.__breed = breed


dog = Dog("Jacky", 2, "Pitbull")

print("dog name is: ", dog.getName)
print("dog age is: " , dog.getAge)
print("Dog breed is: ", dog.getBreed)
