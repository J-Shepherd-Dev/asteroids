import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self)
        # Add to containers if they exist
        if hasattr(self, "containers"):
            self.add(self.containers)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    def collision(self, other, dt):
    # Calculate current and future distance between centers
        current_distance = self.position.distance_to(other.position)
    
    # Predict positions after a small time step
        future_position_self = self.position + self.velocity * dt
        future_position_other = other.position + other.velocity * dt
        future_distance = future_position_self.distance_to(future_position_other)

    # If future distance is less than or equal to sum of radii, they're on collision course
        return future_distance <= (self.radius + other.radius) or current_distance <= (self.radius + other.radius)