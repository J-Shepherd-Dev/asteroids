import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position, velocity):
        # Unpack the position vector into x and y coordinates
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity
    
    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)