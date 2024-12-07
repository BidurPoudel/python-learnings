
class Person:
    def __init__(self, name:str, age: int):
        self.name= name
        self.age = age
        

    def __str__(self) -> str:
        # print(self.name)
        return self.name

    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"
    
person = Person('bidur', 43)
print(person)
print(repr(person))


class Addition:
    def __init__(self, *args):
         self.args = args
    
    def __repr__(self) -> str:
        return f'{self.args}'    

add = Addition(1, 'hi', False)
print(add)