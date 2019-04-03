class Rectangle:
    # constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def square(cls, side_length):
        return cls(side_length, side_length)

print(Rectangle(5,4).calculate_area())

print(Rectangle.square(5).calculate_area())