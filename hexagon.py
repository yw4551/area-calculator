from calculator import Shape
import math


class Hexagon(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return round((3 * math.sqrt(3) * (self.side**2)) / 2, 2)

    def get_perimeter(self):
        return self.side * 6


h = Hexagon(5)
print(h)
