import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Only call super().__init__ once
        super().__init__(x, y, radius)
        self.add(self.containers)  
        # Add rect for collision detection
        self.rect = pygame.Rect(x - radius, 
                              y - radius,
                              radius * 2, 
                              radius * 2)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        # Update rect position
        self.rect.center = (self.position.x, self.position.y)