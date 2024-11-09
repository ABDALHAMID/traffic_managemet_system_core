import pygame
from abc import ABC, abstractmethod

from simulation.Enums import TargetExit
from simulation.Prefabs.TrafficLight import TrafficLight, TrafficLightState
from simulation.simulationSystemBack.SimulationObject import SimulationObject


# class PositionCheckerType(Enum):
#     CHECKEND = "check end"
#     CHECKSTART = "check start"
#     CHECKSTOP = "check stop"
#     CHECKDIRECTION = "check direction"


class PositionChecker(SimulationObject, ABC):
    carFinishedCount = 0
    def __init__(self,
                 position: tuple[float, float],
                 size: tuple[float, float],
                 direction: float,
                 color: tuple[int, int, int, int] | str):
        super().__init__(position, size, direction, color)

    def draw(self, screen):
        super().draw(screen)
    @abstractmethod
    def check_collision_with_vehicles(self, cars):
        pass


class PositionEndChecker(PositionChecker):
    def __init__(self,
                 position: tuple[float, float],
                 size: tuple[float, float],
                 direction: float):
        color = (255, 0, 0, 128)
        super().__init__(position= position, size=size, direction=direction, color=color)

    def check_collision_with_vehicles(self, vehicles):
        for vehicle in vehicles:
            if self.rect.colliderect(vehicle.rect):
                vehicles.remove(vehicle)
                PositionChecker.carFinishedCount+=1


class PositionStartChecker(PositionChecker):
    def __init__(self,
                 position: tuple[float, float],
                 size: tuple[float, float],
                 direction: float):
        color = (0, 255, 0, 128)
        super().__init__(position=position, size=size, direction=direction, color=color)


    def check_collision_with_vehicles(self, cars):
        pass

class PositionStopChecker(PositionChecker):
    def __init__(self,
                 position: tuple[float, float],
                 size: tuple[float, float],
                 direction: float,
                 traffic_light: TrafficLight):
        color = (255, 255, 255, 128)
        self.trafficLight = traffic_light
        super().__init__(position= position, size=size, direction=direction, color=color)

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
    def __init__(self,
                 position: tuple[float, float],
                 size: tuple[float, float],
                 direction: float,
                 direction_checker_exit_type: TargetExit,
                 affected_direction: float,
                 rotation_speed = 1):
        self.direction_checker_exit_type: TargetExit = direction_checker_exit_type
        self.rotation_speed = rotation_speed
        self.affected_direction = affected_direction
        if self.direction_checker_exit_type == TargetExit.FIRST_EXIT:
            color = (0, 0, 255, 128)
        elif self.direction_checker_exit_type == TargetExit.FIRST_EXIT:
            color = (0, 255, 255, 128)
        elif self.direction_checker_exit_type == TargetExit.FIRST_EXIT:
            color = (0, 255, 255, 128)
        else:
            color = (255, 255, 0, 128)

        super().__init__(position=position, size=size, direction=direction, color=color)

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
