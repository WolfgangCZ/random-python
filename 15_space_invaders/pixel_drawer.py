from body import Body
import pygame


class PixelDrawer:
    def __init__(self, screen, pixel_size):
        self.screen = screen
        self.pixel_size = pixel_size

    def draw(self, body: Body):
        for i in range(body.width):
            for j in range(body.height):
                if body.shape[j][i] == 1:
                    pygame.draw.rect(self.screen, "white",
                                     (body.pos.x + i*self.pixel_size,
                                      body.pos.y + j*self.pixel_size,
                                      self.pixel_size, self.pixel_size))
