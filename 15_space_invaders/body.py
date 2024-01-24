from pygame.math import Vector2


class Body:
    def __init__(self, shape: list, pos: Vector2):
        # TODO check for body shape
        self.shape = shape
        self.width = len(self.shape[0])
        self.height = len(self.shape)
        self.pos = pos
