import pygame
import random
from Vehicle import Vehicle
from simulation.positionChecker import PositionChecker, PositionStartChecker
from typing import List


class Spawner:
    def __init__(self, spawn_positions: List[PositionChecker], car_list, interval=2000):
        self.spawn_positions = spawn_positions
        print(self.spawn_positions)
        self.car_list = car_list
        self.interval = interval
        self.last_spawn_time = pygame.time.get_ticks()  # Get the current time for timer tracking

    def spawn_car(self):
        # Choose a random position from the available spawn positions
        span_pos : PositionStartChecker = random.choice(self.spawn_positions)
        position = span_pos.position
        direction = span_pos.direction
        # Create a new car at that position with random attributes
        new_car = Vehicle(start_pos=position, speed=random.randint(5, 10), direction=direction)
        # Add the new car to the list of cars
        self.car_list.append(new_car)

    def update(self, event):
        # Check if the space bar is pressed
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            self.spawn_car()

        # Check if enough time has passed since the last spawn
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time >= self.interval:
            self.spawn_car()
            self.last_spawn_time = current_time  # Reset the timer
