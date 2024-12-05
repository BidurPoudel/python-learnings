class IPerson:
    def details(self, name:str, age:int):
        pass
    
class ICollege:
    def college_details(self, name:str):
        pass
    
class Students(IPerson, ICollege):
    
    def details(self, name , age):
        print(f"name of student is {name} and {age}")
    
  

class College(ICollege):
    def college_details(self, name):
        print(f'name of the college is {name}')


student = Students()
college =College()

student.details('Bidur', 23)
student.college_details('Informatics')