import random

import pygame
import math

from simulation.Enums import TargetExit


class Vehicle(pygame.sprite.Sprite):
    def __init__(self, start_pos, speed=2, direction=0, image_path="C:/Users/ABDVO/OneDrive/Documents/GitHub/traffic_managemet_system_core/cars/red_car.png", size=(60, 35)):
        super().__init__()

        # Load and scale the image
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, size)  # Resize the car image

        # Rotate the image to face the initial direction
        self.image = pygame.transform.rotate(self.original_image, -direction)
        self.rect = self.image.get_rect(center=start_pos)

        # Set initial attributes
        self.position = pygame.Vector2(start_pos)
        self.size = size
        self.traffic_light_rect = self.rect
        self.traffic_light_rect.width = int(self.rect.width * 10 / 100)
        self.original_speed = speed  # Keep the original speed for resuming after stopping
        self.speed = speed
        self.start_direction = direction
        self.direction = direction  # Angle in degrees
        self.shouldStop = False
        self.targetExit = random.choice(list(TargetExit))


        #test
        self.center = self.rect
    def detect_car_ahead(self, other_cars, stopping_distance=80):
        """
        Check if there's another car within stopping distance in front of this car.

        Args:
            other_cars (list of Vehicle): List of other cars in the simulation.
            stopping_distance (int): Distance within which the car should stop.
        """
        for other in other_cars:
            if other == self:
                continue  # Skip self

            # Calculate the vector to the other car
            distance_vector = other.position - self.position
            distance = distance_vector.length()

            # Calculate the angle between the car's direction and the vector to the other car
            angle_to_other = math.degrees(math.atan2(distance_vector.y, distance_vector.x))
            angle_difference = abs((self.direction - angle_to_other + 180) % 360 - 180)

            # Stop if another car is close and within the same direction
            if distance < stopping_distance and angle_difference < 45:
                return True

        # Resume original speed if no car is ahead
        return False

    def update(self, other_cars):
        # Check for cars ahead and adjust speed accordingly
        if self.detect_car_ahead(other_cars) or self.shouldStop:
            self.speed = 0
        else:
            self.speed = self.original_speed

        # Calculate movement based on the current direction
        radian_angle = math.radians(self.direction)
        self.position.x += self.speed * math.cos(radian_angle)
        self.position.y += self.speed * math.sin(radian_angle)

        # Update the rect's position to follow the vector position
        self.rect.center = self.position
        self.traffic_light_rect.center = self.position

    def turn(self, angle_delta):
        # Adjust direction and rotate the image
        self.direction = (self.direction + angle_delta) % 360
        self.image = pygame.transform.rotate(self.original_image, -self.direction)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, screen):
        # Blit the car image at its current position
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (50, 50, 250), self.traffic_light_rect)
        pygame.draw.circle(screen, (0, 255, 0), self.rect.center, 1)
