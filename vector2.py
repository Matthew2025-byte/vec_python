from math import sqrt
class vec2:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    def base_unit_al_rep(self):
        return f"<{self.x}i + {self.y}j>"
    def al_rep(self):
        return f"<{self.x}, {self.y}>"



    def sqrmagnitude(self):
        return self.x**2 + self.y**2
    def magnitude(self):
        return sqrt(self.x**2 + self.y**2)

    def normalized(self):
        return self / self.magnitude()



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
    
    @staticmethod
    def from_polar(magnitude, degrees):
        from math import sin, cos, radians
        a = magnitude * cos(radians(degrees))
        b = magnitude * sin(radians(degrees))
        return vec2(a, b)