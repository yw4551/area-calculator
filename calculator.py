class Shape:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def validate_positive(value, name="Value"):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError(f"{name} must be a number")

        if value <= 0:
            raise ValueError(f"{name} must be a positive number")

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def __str__(self):
        return f"Shape: {self.name}\nArea: {self.get_area()}\nPerimeter: {self.get_perimeter()}\n"

    def __repr__(self):
        attributes = ", ".join(
            f"{k}={v}" for k, v in self.__dict__.items() if k != "name"
        )
        return f"{self.__class__.__name__}({attributes})"
