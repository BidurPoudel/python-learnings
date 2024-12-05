class Shape:
    def area(self) -> float:
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side: float):
        self.side = side
    def area(self) -> float:
        return self.side * self.side
    
# Test the behavior
shapes = [
    Rectangle(4, 5),
    Square(4)
]

for shape in shapes:
    print(f"Area: {shape.area()}")
