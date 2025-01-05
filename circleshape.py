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
    def collision(self, other):
    # Calculate distance between centers using Vector2's distance_to
        distance = self.position.distance_to(other.position)
    # If distance is less than sum of radii, they're colliding
        return distance <= (self.radius + other.radius)