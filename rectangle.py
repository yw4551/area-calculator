from calculator import Shape


class Rectangle(Shape):

    def __init__(self, width, height, name="rectangle"):
        super().__init__(name=name)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.height + self.width) * 2
