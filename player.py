from circleshape import *
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

        self.score = 0  # Player's score

        self.timer = 0  # Timer for shooting cooldown
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d]or keys[pygame.K_RIGHT]:
            self.rotate(dt) 
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move
        if keys[pygame.K_SPACE] and self.timer <= 0:  # Check if the timer is less than or equal to zero
            self.timer = PLAYER_SHOOT_COOLDOWN  # Reset the timer to the cooldown value
            self.shoot()

        self.timer -= dt  # Decrease the timer by the time delta
   

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        position = self.position + forward * (self.radius + SHOT_RADIUS)
        shot = Shot(position.x, position.y, SHOT_RADIUS)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        return shot
    
    def draw(self, screen):        
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):        
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):      
        
        self.position += self.velocity * dt
    