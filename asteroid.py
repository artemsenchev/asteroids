from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):        
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):      
        
        self.position += self.velocity * dt

    def split(self, player):
        self.kill()
        player.score += 1
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # split into two smaller asteroids
            angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            Asteroid(self.position.x, self.position.y, new_radius).velocity = v1 * 1.2
            Asteroid(self.position.x, self.position.y, new_radius).velocity = v2 * 1.2