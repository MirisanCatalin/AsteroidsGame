from constants import *
from circleshape import CircleShape
import pygame

class Bomb(CircleShape):
    def __init__(self, x, y,radius):
        super().__init__(x, y, BOMB_RADIUS)
        self.lifetime = BOMB_LIFETIME
    
    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)
    
    def update(self, dt):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
