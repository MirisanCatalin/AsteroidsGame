from circleshape import CircleShape
from constants import *
from shot import Shot
from bomb import Bomb
from explosion import Explosion
from brick import Brick
from laser import Laser
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS * 0.75)
        self.rotation = 0
        self.shoot_cooldown = 0
        self.bomb_cooldown = 0
        self.gun_type = 1
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def accelerate(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * PLAYER_ACCELERATION * dt
        if self.velocity.length() > PLAYER_MAX_SPEED:
            self.velocity.scale_to_length(PLAYER_MAX_SPEED)

    def shoot_gun(self, gun_type):
        if self.shoot_cooldown > 0:
            return None
        else:
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        if gun_type == 1:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = forward * PLAYER_SHOOT_SPEED
        if gun_type == 2:
            shot = Laser(self.position.x, self.position.y, SHOT_RADIUS)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = forward * PLAYER_SHOOT_SPEED
        if gun_type == 3:
            shot = Brick(self.position.x, self.position.y,SHOT_RADIUS)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = forward * PLAYER_SHOOT_SPEED

    def place_bomb(self):
        if self.bomb_cooldown > 0:
            return None
        else:
            self.bomb_cooldown = PLAYER_PLACE_BOMB_COOLDOWN
        bomba = Bomb(self.position.x, self.position.y, BOMB_RADIUS)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        bomba.velocity = forward * PLAYER_SHOOT_SPEED

    def update(self, dt):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt
        if self.bomb_cooldown > 0:
            self.bomb_cooldown -= dt

        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH            
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot_gun(self.gun_type)
        if keys[pygame.K_b]:
            self.place_bomb()
        if keys[pygame.K_LSHIFT]:
            self.accelerate(dt)
        if keys[pygame.K_1]:
            self.gun_type = 1
        if keys[pygame.K_2]:
            self.gun_type = 2
        if keys[pygame.K_3]:
            self.gun_type = 3
