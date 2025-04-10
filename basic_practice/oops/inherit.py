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




# understanding to calling of private variable from Parent class to child class

class Person:
    def __init__(self, name:str, age:int):
        self.__name:str = name
        self.__age:int= age
    
    def getName(self):
        print(self.__name)
        return self.__name
    
    def setName(self, name:str):
        self.__name = name



class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.__section= section

    def studentSection(self):
        print(f'{self.getName()} is from {self.__section}')

class Teacher(Person):
        def __init__(self, name, age, subject):
            super().__init__(name, age)
            self.__subject= subject

        def teacherSub(self):
            print(f'{self.getName()} teaches {self.__subject}')

student=Student('bidur', 23, 'B')

student.getName() #student object can call function of class Person

student.studentSection()
teacher=Teacher('Shiva', 'UNKNOWN', 'Python')
teacher.teacherSub()

# """when variable is private, if we want to call them from child class we should call the getter method of
# parent class like

# getName(): > it is from person class
# calling it in child class like  print(f'{self.getName()} teaches {self.__subject}')

# """
