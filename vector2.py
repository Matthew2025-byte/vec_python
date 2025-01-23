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



    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return vec2(self.x * other, self.y * other)
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return vec2(self.x / other, self.y / other)

    def __add__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x - other.x, self.y - other.y)