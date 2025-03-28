import random

from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
from random import Random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        split_angle = random.uniform(20.0, 50.0)
        split_vector_high = self.velocity.rotate(split_angle)
        split_vector_low = self.velocity.rotate(-split_angle)

        split_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS


        self.spawn(split_asteroid_radius,self.position, split_vector_low * 1.2)
        self.spawn(split_asteroid_radius, self.position, split_vector_high * 1.2)

        self.kill()
