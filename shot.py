from constants import *
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
        self.lifetime = SHOT_LIFETIME
    
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius,2)
    
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
