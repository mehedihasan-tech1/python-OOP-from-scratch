"""super() = Function used in a child class to call methods from a parent class (superclass).
    allows you to extend the functionality of the inherited methods
"""


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(
            f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"The circle area is {3.14 * self.radius * self.radius}")


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"The square area is {self.width * self.width}")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"The triangle area is {0.5 * self.width * self.height}")


circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="blue", is_filled=False, width=6, height=4)

print(circle.color)
print(f"{square.width} cm")
print(f"{triangle.height} cm")
circle.describe()
