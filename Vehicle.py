import pygame
import math


class Vehicle(pygame.sprite.Sprite):
    def __init__(self, start_pos, speed=2, direction=0, image_path="./cars/red_car.png", size=(60, 35)):
        super().__init__()

        # Load and scale the image
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, size)  # Resize the car image
        self.image = self.original_image  # This will be the rotated image
        self.rect = self.image.get_rect(center=start_pos)

        # Set initial attributes
        self.position = pygame.Vector2(start_pos)
        self.speed = speed
        self.direction = direction  # Angle in degrees

    def update(self):
        # Calculate movement based on the current direction
        radian_angle = math.radians(self.direction)
        self.position.x += self.speed * math.cos(radian_angle)
        self.position.y += self.speed * math.sin(radian_angle)

        # Update the rect's position to follow the vector position
        self.rect.center = self.position

    def turn(self, angle_delta):
        # Adjust direction and rotate the image
        self.direction = (self.direction + angle_delta) % 360
        self.image = pygame.transform.rotate(self.original_image, -self.direction)
        self.rect = self.image.get_rect(center=self.rect.center)
