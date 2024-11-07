import math

import pygame

from simulation.TrafficLight import TrafficLight, TrafficLightState
from simulation.positionChecker import PositionStopChecker


class Road:
    def __init__(self,
                 position,
                 size,
                 direction,
                 startingStatus: TrafficLightState,
                 vehivles,
                 ):
        self.position = position
        self.size = size
        self.direction = direction
        self.startingStatus = startingStatus
        self.vehivles = vehivles

        self.trafficLight = TrafficLight((self.position[0] - 20, self.position[1] + self.size[1]),
                                     self.startingStatus)

        self.positionStopChecker = PositionStopChecker((self.position[0] + math.cos(math.radians(self.direction)) * self.size[0]/2,
                                                        self.position[1] + math.sin(math.radians(self.direction)) * self.size[1]/2),
                                                       (10, self.size[1]),
                                                       self.trafficLight)

    def draw(self, screen):
        # Load the road image (assuming you have a road image path set)
        road_image = pygame.image.load("C:/Users/ABDVO/OneDrive/Documents/GitHub/traffic_managemet_system_core/assets/images/roads/road.png").convert_alpha()
        road_image = pygame.transform.scale(road_image, self.size)

        # Rotate the road image to the correct direction
        rotated_road_image = pygame.transform.rotate(road_image, -self.direction)

        if self.direction < 180:
            road_rect = rotated_road_image.get_rect(center=self.position)
        else:
            road_rect = rotated_road_image.get_rect(center=self.position)

        # Draw the rotated road image on the screen
        screen.blit(rotated_road_image, road_rect.topleft)

        # Draw the traffic light
        self.trafficLight.draw(screen)

        # Draw the position stop checker aligned with the road's direction
        self.positionStopChecker.draw(screen, self.direction)

    def update(self):
        pass

    def calcPos(self):
        position:(float, float)
        radian_angle = math.radians(self.direction)
        position[0] += selfmath.cos(radian_angle)
        position[1] += math.sin(radian_angle)

