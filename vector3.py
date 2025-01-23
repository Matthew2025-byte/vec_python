from math import sqrt
class vec3:
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    

    def sqrmagnitude(self):
        return self.x**2 + self.y**2 + self.z**2
    def magnitude(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalized(self):
        self / self.magnitude()


    

