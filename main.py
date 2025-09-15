import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from bomb import Bomb
from explosion import Explosion

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
    explosions = pygame.sprite.Group()
    
    # Set containers BEFORE creating objects
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroid)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, bullet)
    Bomb.containers = (updatable, drawable, bomba)
    Explosion.containers = (updatable, drawable, explosions)
    # Create game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    
    dt = 0
    player_score = 0
    lives = PLAYER_STARTING_LIVES

    bg = pygame.image.load("space_background.png").convert()
    
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
        #screen.fill("black")
        
        screen.blit(bg, (0, 0))
        # Check collisions BEFORE drawing
        
        explosions.draw(screen)
        explosions.update()

        for aster in asteroid:
            if player.collision_with(aster):
                
                for aster in asteroid:
                    aster.kill()
                player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                
                lives -= 1
       
        for aster in asteroid:
            for shot in bullet:
                if aster.collision_with(shot):
                    pos = aster.position
                    explo = Explosion(pos.x, pos.y)
                    explosions.add(explo)
                    shot.kill()
                    player_score += aster.split()
            for bom in bomba:
                if aster.collision_with(bom):
                    pos = aster.position
                    explo = Explosion(pos.x, pos.y)
                    explosions.add(explo)
                    bom.kill()
                    player_score += aster.split()

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

        gun_text = my_font.render('Press 1: Gun', True, (255, 255, 255))
        laser_text = my_font.render('Press 2: Laser', True, (255, 255, 255))
        brick_text = my_font.render('Press 3: Brick', True, (255, 255, 255))
        screen.blit(gun_text, (SCREEN_WIDTH - 200, 10))
        screen.blit(laser_text, (SCREEN_WIDTH - 200, 50))
        screen.blit(brick_text, (SCREEN_WIDTH - 200, 90))

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
        game_over = my_font.render(f"Game Over Current score {player_score}", True, (0, 0, 0))
        screen.blit(game_over, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50))

        pygame.display.flip()

if __name__ == "__main__":
    main()
