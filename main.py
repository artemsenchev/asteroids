import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    pygame.init()

    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    fps = 60

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # Clear the screen with black

        # Update the game state
        player.draw(screen)
        player.update(dt)

        pygame.display.flip() #flip/update the display: make the drawn content visible

        

        time_passed = game_clock.tick(fps)  # Maintain the game at a constant FPS
        dt = time_passed / 1000.0  # Convert milliseconds to seconds



if __name__ == "__main__":
    main()