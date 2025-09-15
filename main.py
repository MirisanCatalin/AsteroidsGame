import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from bomb import Bomb

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    
    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    bullet = pygame.sprite.Group()
    bomba = pygame.sprite.Group()
    
    # Set containers BEFORE creating objects
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroid)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, bullet)
    Bomb.containers = (updatable, drawable, bomba)

    # Create game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    
    dt = 0
    player_score = 0
    lives = PLAYER_STARTING_LIVES
    
    # Load highscore (with error handling)
    try:
        with open("highscore.txt", "r") as f:
            highscore = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        highscore = 0
    
    while lives > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update all objects
        updatable.update(dt)
        
        # Clear screen
        screen.fill("black")
        
        # Check collisions BEFORE drawing
        for aster in asteroid:
            if player.collision_with(aster):
                
                for aster in asteroid:
                    aster.kill()
                player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                
                lives -= 1
        
        for shot in bullet:
            for aster in asteroid:
                if shot.collision_with(aster):
                    shot.kill()
                    player_score += aster.split()

        for boom in bomba:
            for aster in asteroid:
                if boom.collision_with(aster):
                    player_score += aster.split()
                boom.kill()
        
        # Draw all objects
        for obj in drawable:
            obj.draw(screen)
        
        # Draw UI text (AFTER clearing screen, BEFORE display.flip())
        score_text = my_font.render(f'Score: {player_score}', True, (255, 255, 255))
        highscore_text = my_font.render(f'High Score: {highscore}', True, (255, 255, 255))
        lives_text = my_font.render(f'Lives: {lives}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(highscore_text, (10, 50))
        screen.blit(lives_text, (10, 90))
        
        # Update highscore if needed
        if player_score > highscore:
            highscore = player_score
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
        
        # Update display
        pygame.display.flip()
        pygame.display.set_caption(f"Asteroids - Score: {player_score} Highscore: {highscore}")
        
        # Limit framerate
        dt = clock.tick(60) / 1000

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Update all objects
        updatable.update(dt)
        # Clear screen
        screen.fill("black")
        # Draw all objects
        game_over = my_font.render(f"Game Over\nCurrent score {player_score}", True, (255, 0, 0))
        screen.blit(game_over, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50))

        pygame.display.flip()

if __name__ == "__main__":
    main()
