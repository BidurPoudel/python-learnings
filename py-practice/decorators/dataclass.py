from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
user = User("bidur", 21)
print(user.age)