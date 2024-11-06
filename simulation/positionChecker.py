import pygame
from enum import Enum
from abc import ABC, abstractmethod

from simulation.Enums import TargetExit
from simulation.TrafficLight import TrafficLight, TrafficLightState

# class PositionCheckerType(Enum):
#     CHECKEND = "check end"
#     CHECKSTART = "check start"
#     CHECKSTOP = "check stop"
#     CHECKDIRECTION = "check direction"


class PositionChecker(ABC):
    carFinishedCount = 0
    def __init__(self, position, size):
        self.position = position
        self.size = (size[0], size[1])
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    @abstractmethod
    def draw(self, screen):
        pass
    @abstractmethod
    def check_collision_with_vehicles(self, cars):
        pass


class PositionEndChecker(PositionChecker):
    def __init__(self, position, size):
        super().__init__(position= position, size=size)

    def draw(self, screen):
        checker_surface = pygame.Surface(self.size, pygame.SRCALPHA)
        color = pygame.Color(255, 0, 0, 128)
        checker_surface.fill(color)
        screen.blit(checker_surface, self.position)

    def check_collision_with_vehicles(self, vehicles):
        for vehicle in vehicles:
            if self.rect.colliderect(vehicle.rect):
                vehicles.remove(vehicle)
                PositionChecker.carFinishedCount+=1


class PositionStartChecker(PositionChecker):
    def __init__(self, position, size, direction = 0):
        super().__init__(position=position, size=size)
        self.direction = direction


    def draw(self, screen):
        checker_surface = pygame.Surface(self.size, pygame.SRCALPHA)
        color = pygame.Color(0, 0, 255, 128)
        checker_surface.fill(color)
        screen.blit(checker_surface, self.position)

    def check_collision_with_vehicles(self, cars):
        pass

class PositionStopChecker(PositionChecker):
    def __init__(self, position, size, traffic_light: TrafficLight):
        super().__init__(position=position, size=size)
        self.trafficLight = traffic_light

    def draw(self, screen):
        checker_surface = pygame.Surface(self.size, pygame.SRCALPHA)
        color = pygame.Color(255, 255, 255, 128)
        checker_surface.fill(color)
        screen.blit(checker_surface, self.position)

    def check_collision_with_vehicles(self, vehicles):
        for vehicle in vehicles:
            if self.rect.colliderect(vehicle.rect):
                if self.trafficLight.state == TrafficLightState.RED:
                    vehicle.shouldStop = True
                elif self.trafficLight.state == TrafficLightState.GREEN:
                    vehicle.shouldStop = False
                else:
                    vehicle.shouldStop = True


class PositionDirectionChecker(PositionChecker):
    def __init__(self, position, size, affected_direction, direction_checker_exit_type: TargetExit, rotation_speed = 1):
        super().__init__(position=position, size=size)
        self.direction_checker_exit_type: TargetExit = direction_checker_exit_type
        self.rotation_speed = rotation_speed
        self.affected_direction = affected_direction

    def draw(self, screen):
        checker_surface = pygame.Surface(self.size, pygame.SRCALPHA)
        if self.direction_checker_exit_type == TargetExit.FIRST_EXIT:
            color = pygame.Color(0, 0, 255, 128)
        elif self.direction_checker_exit_type == TargetExit.FIRST_EXIT:
            color = pygame.Color(0, 255, 255, 128)
        elif self.direction_checker_exit_type == TargetExit.FIRST_EXIT:
            color = pygame.Color(0, 255, 255, 128)
        else:
            color = pygame.Color(255, 255, 0, 128)
        checker_surface.fill(color)
        screen.blit(checker_surface, self.position)

    def check_collision_with_vehicles(self, vehicles):
        for vehicle in vehicles:
            # Only process if the vehicle hasn't collided yet
            if (not vehicle.has_collided and
                    self.rect.colliderect(vehicle.rotated_traffic_light_rect) and
                    vehicle.start_direction == self.affected_direction):
                vehicle_target_exit = vehicle.targetExit
                if self.direction_checker_exit_type == vehicle_target_exit:
                    vehicle.target_direction = vehicle.direction + self.direction_checker_exit_type.value
                    # Mark the vehicle as collided for this cycle
                    vehicle.has_collided = True
