from turtledemo.penrose import start

import pygame
import random

from Vehicle import Vehicle

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class TrafficSimulation:
    def __init__(self):
        # Initialize Pygame and the screen
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Roundabout Traffic Light Simulation")

        # Clock to control FPS
        self.clock = pygame.time.Clock()
        self.running = True


    def run(self):
        car1 = Vehicle(start_pos=pygame.Vector2(40, 40), speed=5)
        car1.draw(self.screen)
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(WHITE)
            self.clock.tick(30)
            pygame.display.update()

        pygame.quit()


# Create and run the simulation
simulation = TrafficSimulation()
simulation.run()
