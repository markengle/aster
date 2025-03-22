# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_clock = pygame.time.Clock()
    dt = 0
    player01 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    continue_game_loop = True
    while continue_game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()
        local_delta = game_clock.tick(60)
        dt = (local_delta / 1000)
        player01.draw(screen)




if __name__ == "__main__":
    main()