import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import *
import time


def displayScore(score, font, screen):
   
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.topright = (SCREEN_WIDTH-10, 0) #width, 0 is the top right corner.
    
    screen.blit(text, text_rect)

def main():
    print("Starting Asteroids!")
    pygame.init()
    pygame.font.init()


    font = pygame.font.SysFont('Arial', 24)
    
    

    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    fps = 60

    updateable_group = pygame.sprite.Group() # This is a list of objects that need to be updated every frame
    drawable_group = pygame.sprite.Group() # This is a list of objects that need to be drawn every frame
    asteroids_group = pygame.sprite.Group() # This is a list of asteroids that need to be updated every frame
    shot_group = pygame.sprite.Group() # This is a list of shots that need to be updated every frame

    Player.containers = (updateable_group, drawable_group)  # Set the containers for the Player class
    Asteroid.containers = (asteroids_group, drawable_group, updateable_group)  # Set the containers for the Asteroids class
    AsteroidField.containers = (updateable_group)  # Set the containers for the AsteroidField class
    Shot.containers = (shot_group, updateable_group, drawable_group)  # Set the containers for the Shot class

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # Clear the screen with black   
        
        

        for sprite in drawable_group:
            sprite.draw(screen)

        updateable_group.update(dt)



        for asteroid in asteroids_group:
            if asteroid.collide(player):
                print("Game over!")
                time.sleep(1)
                exit()

            for shot in shot_group:
                if asteroid.collide(shot):
                    print("Hit!")
                    asteroid.split(player)
                    shot.kill()
                    
        displayScore(str(player.score), font, screen)
        pygame.display.flip() #flip/update the display: make the drawn content visible

        

        time_passed = game_clock.tick(fps)  # Maintain the game at a constant FPS
        dt = time_passed / 1000.0  # Convert milliseconds to seconds



if __name__ == "__main__":
    main()