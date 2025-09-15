from shot import Shot
from constants import *
import pygame

class Brick(Shot):
    def __init__(self, x, y,radius):
        super().__init__(x, y, SHOT_RADIUS * 2)
        self.lifetime = SHOT_LIFETIME * 2

    def draw(self, screen):
        pygame.draw.rect(screen, "brown", (self.position.x - 10, self.position.y - 10, 20, 20))
    
    def update(self, dt):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
            return
        self.position += self.velocity * dt
        # do not warp, just kill if out of screen
        if self.position.x < 0:
            self.kill()
        elif self.position.x > SCREEN_WIDTH:
            self.kill()
        if self.position.y < 0:
            self.kill()
        elif self.position.y > SCREEN_HEIGHT:
            self.kill()
