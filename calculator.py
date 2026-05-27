class Shape:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def validate_positive(value, name="Value"):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TabError(f"{name} must be a number")

        if value <= 0:
            raise ValueError(f"{name} must be a positive number")

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def __str__(self):
        return f"This is a {self.name} with an area of {self.get_area()} and a perimeter of {self.get_perimeter()}"
