import pygame
import sys
from asteroid import Asteroid
import asteroid
from constants import *
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from logger import log_event
from shot import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)

    dt = 0.0
    asteroidfield = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for aster in asteroids:
            if player.collides_with(aster):
                log_event("player_hit")
                print("GAME OVER!")
                sys.exit()
            for shot in shots:
                if aster.collides_with(shot):
                    log_event("asteroid_shot")
                    aster.split()
                    shot.kill()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
