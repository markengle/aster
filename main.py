import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shots_group, updatable_group, drawable_group)

    asteroidfield = AsteroidField()
    player01 = Player(x, y)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        dt = (game_clock.tick(60) / 1000)

        for updatable in updatable_group:
            updatable.update(dt)

        for asteroid in asteroids_group:
            if asteroid.is_colliding(player01):
                print("Game Over!")
                return

        for asteroid in asteroids_group:
            for shot in shots_group:
                if shot.is_colliding(asteroid):
                    asteroid.split()
                    shot.kill()

        for drawable in drawable_group:
            drawable.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()