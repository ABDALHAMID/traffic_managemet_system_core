import random
import pygame
import math
from simulation.Enums import TargetExit

class Vehicle(pygame.sprite.Sprite):
    def __init__(self,
                 start_pos,
                 image_path,
                 speed=2,
                 direction=0,
                 size=(45, 23)):
        super().__init__()

        # Load and scale the image
        self.target_direction = None
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, size)

        # Rotate the image to face the initial direction
        self.image = pygame.transform.rotate(self.original_image, -direction)
        self.rect = self.image.get_rect(center=start_pos)

        # Set initial attributes
        self.position = pygame.Vector2(start_pos)
        self.size = size
        self.traffic_light_offset = self.size[0] / 2  # Distance in pixels for traffic light in front of vehicle
        self.traffic_light_rect_size = (self.size[0] * 0.15, self.size[1])  # Adjust traffic light size
        self.original_speed = speed
        self.speed = speed
        self.start_direction = direction
        self.direction = direction  # Angle in degrees
        self.shouldStop = False
        self.targetExit = random.choice(list(TargetExit))
        self.turning_speed = 3
        self.has_collided = False

        # Create the traffic light surface
        self.traffic_light_surface = pygame.Surface(self.traffic_light_rect_size, pygame.SRCALPHA)
        self.traffic_light_surface.fill((0, 255, 255, 128))  # Color with transparency

        self.rotated_traffic_light_rect: pygame.Rect

    def detect_car_ahead(self, other_cars, stopping_distance=55):
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
        elif self.target_direction is not None:
            self.speed = 2.5
        else:
            self.speed = self.original_speed


        if self.target_direction is not None:
            self.turnToDirection(self.target_direction)

        # Calculate movement based on the current direction
        radian_angle = math.radians(self.direction)
        self.position.x += self.speed * math.cos(radian_angle)
        self.position.y += self.speed * math.sin(radian_angle)

        # Update the rect's position to follow the vector position
        self.rect.center = self.position

        # Calculate traffic light position in front of the vehicle
        offset_x = self.traffic_light_offset * math.cos(radian_angle)
        offset_y = self.traffic_light_offset * math.sin(radian_angle)
        self.traffic_light_position = (self.position.x + offset_x, self.position.y + offset_y)

        # Rotate the traffic light surface based on the vehicle's direction
        self.rotated_traffic_light = pygame.transform.rotate(self.traffic_light_surface, -self.direction)
        self.rotated_traffic_light_rect = self.rotated_traffic_light.get_rect(center=self.traffic_light_position)

    def turn(self, angle_delta):
        # Adjust direction and rotate the image
        self.direction = (self.direction + angle_delta) % 360
        self.image = pygame.transform.rotate(self.original_image, -self.direction)
        # Center the rotated rect on the current position
        self.rect = self.image.get_rect(center=self.position)

    def turnToDirection(self, target_direction):
        # Calculate the shortest angle to turn
        angle_diff = (target_direction - self.direction + 360) % 360
        if angle_diff > 180:
            angle_diff -= 360  # Turn in the shorter direction

        # Determine the turning direction and apply smooth rotation
        if angle_diff > 0:
            self.turn(min(self.turning_speed, angle_diff))  # Turn clockwise
        elif angle_diff < 0:
            self.turn(-min(self.turning_speed, -angle_diff))  # Turn counterclockwise

        if self.direction == target_direction:
            self.target_direction = None

    def draw(self, screen):
        # Blit the car image at its current position
        screen.blit(self.image, self.rect)



        # Draw the traffic light rectangle in front of the vehicle
        screen.blit(self.rotated_traffic_light, self.rotated_traffic_light_rect.topleft)

        # Draw a small circle at the car's center for reference
        pygame.draw.circle(screen, (0, 255, 0), self.rect.center, 1)
