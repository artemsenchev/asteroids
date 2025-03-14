import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # Clear the screen with black
        pygame.display.flip() 



if __name__ == "__main__":
    main()