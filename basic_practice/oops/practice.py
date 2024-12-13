

class User:
    
    def __init__(self, name:str, address:str, gender:str):
        self.__name = name
        self.__address = address
        self.__gender = gender
    
    @property
    def getDetails(self):
        return f"{self.__name} {self.__address} {self.__gender}"


    @getDetails.setter
    def setDetails(self, name:str, address:str, gender:str):
        self.__name = name
        self.__address = address
        self.__gender = gender
    

class Students(User):
    def __init__(self, name: str, address: str, gender: str, age: int, grade:str):
        super().__init__(name, address, gender)
        self.__age = age
        self.__grade = grade

    @property
    def get_student_details(self):
        return f"{self.__name}{self.__age}{self.__gender}{self.__grade}{self.__address}"
    

    @get_student_details.setter
    def set_student_details(self, name:str, address:str, gender:str, age:int, grade:str):
        self.__name:str = name
        self.__address:str = address
        self.__gender:str = gender
        self.__age:int = age
        self.__grade:str = grade


user = User("Bidur", "Lakeside", "Male")


stud = Students("Bidur", "Lakeside", "Male", 23, "A")
# print(isinstance(stud, User)) -> True
# print(isinstance(user, Students)) -> false
print(stud.getDetails)

