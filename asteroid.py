import pygame
from circleshape import CircleShape
from constants import *
from logger import *
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        asteroid_angle = random.uniform(20, 50)
        a = self.velocity.rotate(asteroid_angle)
        b = self.velocity.rotate(-asteroid_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid.velocity = a * 1.2
        split_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid.velocity = b * 1.2


            #Asteroid(self.position.x, self.position.y, self.radius)
            #Asteroid(self.position.x, self.position.y, self.radius)
