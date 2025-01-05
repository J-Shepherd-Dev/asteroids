import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

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

    def split(self):
    # Step 1: Kill the current asteroid
        self.kill()

    # Step 2: Check against minimum radius and return if too small
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

    # Step 3: Calculate attributes for two new asteroids

        random_angle = random.uniform(20, 50)

    # Create two velocity vectors based on the random angle
    # Assume self.velocity is a pygame Vector2
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2

    # Calculate the new smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

    # Step 4: Instantiate two smaller asteroids
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

    # Assign velocities to these new asteroids
        new_asteroid1.velocity = new_velocity1
        new_asteroid2.velocity = new_velocity2
        # Ideally, add them to the appropriate group
        # Whatever container or group manages asteroids should add these
        for container in self.containers:
            container.add(new_asteroid1, new_asteroid2)