from shot import Shot
import pygame
from constants import *

class Laser(Shot):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS / 2)
        self.lifetime = SHOT_LIFETIME / 2  # Lasers last half as long as regular shots
    def draw(self, screen):
        pygame.draw.line(screen, "cyan", self.position, self.position + self.velocity.normalize() * 20, 2)
            
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
