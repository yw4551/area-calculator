from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon

shapes = [
    Rectangle(5, 10),
    Square(5),
    Triangle(5, 10, 5, 5, 5),
    Circle(5),
    Hexagon(5),
]

for shape in shapes:
    print(shape)
    print(repr(shape))
