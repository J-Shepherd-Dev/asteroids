# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while(True):
        #Handle events first
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        #Fill the screen with black
        screen.fill((0, 0, 0))
    
        #Update the display
        pygame.display.flip()
    


if __name__ == "__main__":
    main()
