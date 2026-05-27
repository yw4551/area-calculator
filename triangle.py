from rectangle import Rectangle


class Triangle(Rectangle):
    def __init__(self, base, height, side_a, side_b, side_c):
        self.validate_positive(base, "Base")
        self.validate_positive(height, "Height")
        self.validate_positive(side_a, "Side_a")
        self.validate_positive(side_b, "Side_b")
        self.validate_positive(side_c, "Side_c")
        super().__init__(width=base, height=height, name="triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        return super().get_area() / 2

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
