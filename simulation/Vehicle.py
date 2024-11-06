import random
import pygame
import math
from simulation.Enums import TargetExit


class Vehicle(pygame.sprite.Sprite):
    def __init__(self, start_pos, speed=2, direction=0,
                 image_path="C:/Users/ABDVO/OneDrive/Documents/GitHub/traffic_managemet_system_core/cars/red_car.png",
                 size=(60, 35)):
        super().__init__()

        # Load and scale the image
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, size)

        # Rotate the image to face the initial direction
        self.image = pygame.transform.rotate(self.original_image, -direction)
        self.rect = self.image.get_rect(center=start_pos)

        # Set initial attributes
        self.position = pygame.Vector2(start_pos)
        self.size = size
        self.traffic_light_offset = 30  # Distance in pixels for traffic light in front of vehicle
        self.traffic_light_rect_size = (10, 35)  # Adjust traffic light size
        self.original_speed = speed
        self.speed = speed
        self.start_direction = direction
        self.direction = direction  # Angle in degrees
        self.shouldStop = False
        self.targetExit = random.choice(list(TargetExit))

    def detect_car_ahead(self, other_cars, stopping_distance=80):
        """
        Check if there's another car within stopping distance in front of this car.
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

        # Calculate traffic light rect's position in front of the vehicle and center it
        offset_x = self.traffic_light_offset * math.cos(radian_angle)
        offset_y = self.traffic_light_offset * math.sin(radian_angle)
        traffic_light_center_x = self.position.x + offset_x
        traffic_light_center_y = self.position.y + offset_y

        # Center the traffic light rect on the calculated position
        self.traffic_light_rect = pygame.Rect(
            0, 0, *self.traffic_light_rect_size
        )
        self.traffic_light_rect.center = (traffic_light_center_x, traffic_light_center_y)

    def turn(self, angle_delta):
        # Adjust direction and rotate the image
        self.direction = (self.direction + angle_delta) % 360
        self.image = pygame.transform.rotate(self.original_image, -self.direction)
        # Center the rotated rect on the current position
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        # Blit the car image at its current position
        screen.blit(self.image, self.rect)

        # Draw the traffic light rectangle in front of the vehicle
        traffic_light_rect_surface = pygame.Surface(self.traffic_light_rect_size, pygame.SRCALPHA)
        color = pygame.Color(0, 255, 255, 128)
        traffic_light_rect_surface.fill(color)
        screen.blit(traffic_light_rect_surface, self.traffic_light_rect.topleft)

        # Draw a circle at the car's center for reference
        pygame.draw.circle(screen, (0, 255, 0), self.rect.center, 1)
