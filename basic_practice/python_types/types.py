a: int = 1
ab: str = "bidur"
ac:bool = True
ad:float = 1.2
list_of_fruits: list[str] = ["mango", "banana", "grapes"]
 
def get_full_name(first_name:str, last_name:str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name
print(get_full_name("bidur", "poudel"))


#it is tuple types
tup: tuple[str, int] = ("name", 2) 

# it is dictionary type
diction: dict[str, int] = {'bidur': 1}

def process_items(items: list[str]):
    for item in items:
        print(item)


list_of_fruits: list[str] = ["mango", "banana", "grapes"]

process_items(list_of_fruits)


def say_name(name: str| None = None):
    if name is not None:
        print(f"hello {name}")
    else:
        print("Name not found")

name: str = "bidur"

say_name(name)


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


def get_person_name(person: Person):
    return person.age



from typing import Dict, Tuple,Optional, List, Union, FrozenSet,Set

# it is dict typing
user_data: Dict[str, int] = {
    "age": 25,
    "score": 90
}

# tuple typing
person: Tuple[int, str, float] = (25, "Alice", 75.5)
numbers: Tuple[int, ...] = (1, 2, 3, 4)

# Example: List of integers
scores: List[int] = [85, 90, 78]


# Example: Set of strings
unique_names: Set[str] = {"Alice", "Bob", "Charlie"}


# Example: FrozenSet of integers
immutable_set: FrozenSet[int] = frozenset({1, 2, 3})


# Example: List containing both integers and strings
mixed_list: List[Union[int, str]] = [1, "hello", 3, "world"]

# Example: An integer that might be None
age: Optional[int] = None


# for custome object in container
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

users: List[User] = [User("Alice", 30), User("Bob", 25)]
