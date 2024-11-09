import pygame
import random
from simulation.Prefabs.Vehicle import Vehicle
from simulation.Prefabs.positionChecker import PositionChecker, PositionStartChecker
from typing import List


class Spawner:
    totalVehicles = 0
    cars_img = [
        "C:/Users/ABDVO/OneDrive/Documents/GitHub/traffic_managemet_system_core/cars/red_car.png",
        "C:/Users/ABDVO/OneDrive/Documents/GitHub/traffic_managemet_system_core/cars/yellow_car.png",
        "C:/Users/ABDVO/OneDrive/Documents/GitHub/traffic_managemet_system_core/cars/green_car.png",
    ]
    def __init__(self, spawn_positions: List[PositionChecker], car_list, interval=2000):
        self.spawn_positions = spawn_positions
        self.car_list = car_list
        self.interval = interval
        self.last_spawn_time = pygame.time.get_ticks()

    def spawn_car(self):
        # Choose a random position from the available spawn positions
        span_pos : PositionStartChecker = random.choice(self.spawn_positions)
        position = (span_pos.position.x, span_pos.position.y)
        direction = span_pos.direction.direction
        # Create a new car at that position with random attributes
        new_car = Vehicle(start_pos=position,
                          image_path=random.choice(Spawner.cars_img),
                          speed=random.randint(5, 10),
                          direction=direction)
        Spawner.totalVehicles+=1
        # Add the new car to the list of cars
        self.car_list.append(new_car)

    def update(self, event = None):
        # Check if the space bar is pressed
        if  event is not None and event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            self.spawn_car()

        # Check if enough time has passed since the last spawn
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time >= self.interval:
            self.spawn_car()
            self.last_spawn_time = current_time  # Reset the timer
