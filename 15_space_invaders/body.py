from pygame.math import Vector2


class Body:
    def __init__(self, shape: list, pos: Vector2):
        # TODO check for body shape
        self.shape = shape
        self.width = len(self.shape[0])
        self.height = len(self.shape)
        self.pos = pos
    def set_pos_center(self, pos: Vector2):
        self.pos.x = pos.x - self.width/2
        self.pos.y = pos.y - self.height/2
