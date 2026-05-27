class Shape:
    def __init__(self, name):
        self.name = name

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def __str__(self):
        return f"This is a {self.name} with an area of {self.get_area()} and a perimeter of {self.get_perimeter()}"
