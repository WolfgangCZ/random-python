import math

class Vector2:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    def lenght(self) -> float:
        return float(math.sqrt(self.x*self.x + self.y*self.y))
    def normalize(self):
        l = self.lenght()
        t_x = 1/l*self.x
        t_y = 1/l*self.y
        self.x = t_x
        self.y = t_y

vec = Vector2(4,3)


print(vec.x)
print(vec.y)
print(vec.lenght())
vec.normalize()
print(vec.x)
print(vec.y)
print(vec.lenght())