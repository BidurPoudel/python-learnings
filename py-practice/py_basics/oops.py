class Employee:
    # name = "bidur" # class attribute
    # salary = 30000

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def getInfo(self):
        print(f"The name is {self.name} with salary is {self.salary}")
    
    def greetUser(self):
        print(f"Hello! {self.name}")

    @staticmethod
    def information():
        print("hi how are you! ")

bidur = Employee("bidur", 300000);
Bidur = Employee("Bidur", 300000);
# bidur.name = "Bidur Poudel" #object attribute
bidur.getInfo()
Bidur.getInfo()
bidur.greetUser()
