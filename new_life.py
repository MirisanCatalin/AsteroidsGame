import pygame
import random
from constants import *
import math

def draw(self, screen):
    points = star_points(self.position, self.radius, self.radius // 2, num_points=5)
    pygame.draw.polygon(screen, "yellow", points)          # filled
    pygame.draw.polygon(screen, "orange", points, width=2) # outline


class NewLife(pygame.sprite.Sprite):
    def __init__(self, x, y, radius=20):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        cx, cy = int(self.position.x), int(self.position.y)
        color = "yellow"
        pygame.draw.line(screen, color, (cx - self.radius, cy), (cx + self.radius, cy), 2)
        pygame.draw.line(screen, color, (cx, cy - self.radius), (cx, cy + self.radius), 2)
        pygame.draw.line(screen, color, (cx - self.radius//2, cy - self.radius//2),(cx + self.radius//2, cy + self.radius//2), 2)
        pygame.draw.line(screen, color, (cx - self.radius//2, cy + self.radius//2),(cx + self.radius//2, cy - self.radius//2), 2)



    def collision_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

