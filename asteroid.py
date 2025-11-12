import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,
                           self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        direction_angle = random.uniform(20, 50)

        astroid_1_movement = self.velocity.rotate(direction_angle)
        astroid_2_movement = self.velocity.rotate(-direction_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        astroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        astroid_1.velocity = astroid_1_movement * 1.2

        astroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        astroid_2.velocity = astroid_2_movement * 1.2
