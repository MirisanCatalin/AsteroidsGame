# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    player.draw(screen)


    while True:

        screen.fill("black")

        player.draw(screen)

        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        
        pygame.display.set_caption(f"Asteroids - FPS: {clock.get_fps():.2f}")

if __name__ == "__main__":
    main()
