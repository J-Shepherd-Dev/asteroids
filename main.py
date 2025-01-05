# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player_group = pygame.sprite.GroupSingle() 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    AsteroidField()
    Player.containers = (player_group, updatable, drawable)  # Updated to include player_group
    Shot.containers = (shots, updatable, drawable)
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player = player_group.sprite
    while(True):
        #handle the framerate
        dt = clock.tick(60) / 1000
        #Handle events first
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # updates all entities
        for entity in updatable:
            entity.update(dt)
        for asteroid in asteroids:
            collided_shots = pygame.sprite.spritecollide(asteroid, shots, False)
            for shot in collided_shots:
                shot.kill()
                asteroid.split()
            if player.collision(asteroid, dt):
                print("Game over!")
                sys.exit()
        #Fill the screen with black
        screen.fill((0, 0, 0))
        # Draw the player entities
        for entity in drawable:
            entity.draw(screen)
        #Update the display
        pygame.display.flip()

    


if __name__ == "__main__":
    main()
