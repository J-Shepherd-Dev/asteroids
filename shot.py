import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position, velocity):
        # Initialize CircleShape (which handles sprite initialization)
        super().__init__(position.x, position.y, SHOT_RADIUS)
        # Remove pygame.sprite.Sprite.__init__(self) since it's already called
        
        # Add rect for collision detection
        self.rect = pygame.Rect(position.x - SHOT_RADIUS, 
                              position.y - SHOT_RADIUS,
                              SHOT_RADIUS * 2, 
                              SHOT_RADIUS * 2)
        self.velocity = velocity
    
    def update(self, dt):
        self.position += self.velocity * dt
        # Update rect position
        self.rect.center = (self.position.x, self.position.y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)