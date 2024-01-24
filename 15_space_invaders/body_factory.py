from body import Body
from pygame.math import Vector2


class BodyFactory:
    def __init__(self):
        print("initializing body factory")

    def create(self, shape: list, pos: Vector2):
        return Body(shape, pos)
