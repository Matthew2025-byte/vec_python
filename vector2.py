from math import sqrt
class vec2:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def sqrmagnitude(self):
        return self.x**2 + self.y**2
    def magnitude(self):
        return sqrt(self.x**2 + self.y**2)

    def normalized(self):
        self / self.magnitude()