from circleshape import CircleShape
from constants import *
import pygame
import random
import math

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.shape = self.generate_shape() 

    def generate_shape(self):
        points = []
        num_points = 20  # more points = smoother outline
        for i in range(num_points):
            angle = (2 * math.pi / num_points) * i
            noisy_radius = self.radius * (1 + random.uniform(-0.3, 0.3))  # add lumpiness
            x = noisy_radius * math.cos(angle)
            y = noisy_radius * math.sin(angle)
            points.append((x, y))
        return points

#    def draw(self, screen):
#        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def draw(self, screen):
        # Shift local shape points by asteroid position
        translated = [(self.position.x + px, self.position.y + py) for px, py in self.shape]
        pygame.draw.polygon(screen, "white", translated, 5)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            
            new_velocity_1 = self.velocity.rotate(angle)
            new_velocity_2 = self.velocity.rotate(-angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_velocity_1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = new_velocity_2 * 1.2
            if self.radius == ASTEROID_MAX_RADIUS:
                return 4
            else:
                return 2
        else:
            return 1
