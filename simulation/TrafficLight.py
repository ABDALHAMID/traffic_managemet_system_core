import pygame

from enum import Enum

class TrafficLightState(Enum):
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"


class TrafficLight(pygame.sprite.Sprite):
    def __init__(self, position, startState: TrafficLightState, red_duration=10000, green_duration=10000, yellow_duration=3000):
        super().__init__()
        self.position = position
        self.red_duration = red_duration
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.state = startState # Start with red light
        self.timer = pygame.time.get_ticks()  # Timer to track state changes

        # Initial color for drawing
        self.color = pygame.Color(startState.value)
        self.rect = pygame.Rect(position[0], position[1], 35, 35)  # Traffic light size

    def update(self):
        # Get the current time
        current_time = pygame.time.get_ticks()

        # State transition logic based on elapsed time
        if self.state == TrafficLightState.RED and current_time - self.timer >= self.red_duration:
            self.state = TrafficLightState.GREEN
            self.color = pygame.Color("green")
            self.timer = current_time  # Reset timer for the next state
        elif self.state == TrafficLightState.GREEN and current_time - self.timer >= self.green_duration:
            self.state = TrafficLightState.YELLOW
            self.color = pygame.Color("yellow")
            self.timer = current_time
        elif self.state == TrafficLightState.YELLOW and current_time - self.timer >= self.yellow_duration:
            self.state = TrafficLightState.RED
            self.color = pygame.Color("red")
            self.timer = current_time

    def draw(self, screen):
        # Draw the traffic light rectangle (or a more realistic shape)
        pygame.draw.rect(screen, (50, 50, 50), self.rect)  # Draw light housing
        # Draw the circle for the light itself
        pygame.draw.circle(screen, self.color, self.rect.center, 10)
