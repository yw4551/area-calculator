from calculator import Shape
import math


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return round((self.radius**2) * math.pi, 2)

    def get_perimeter(self):
        return round(2 * math.pi * self.radius, 2)
