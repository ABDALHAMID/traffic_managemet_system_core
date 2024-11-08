import pygame

from enum import Enum

from typing_extensions import override

from simulation.simulationSystemBack.SimulationObject import SimulationObject


class TrafficLightState(Enum):
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"


class TrafficLight(SimulationObject):
    def __init__(self,
                 position,
                 direction,
                 start_state: TrafficLightState,
                 size = (35, 35),
                 red_duration=10000,
                 green_duration=10000,
                 yellow_duration=3000):
        base_color = (100, 100, 100, 255)
        super().__init__(position, size, direction, base_color)
        self.red_duration = red_duration
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.state = start_state
        self.timer = pygame.time.get_ticks()


        self.state_color = pygame.Color(start_state.value)

    def update(self):
        # Get the current time
        current_time = pygame.time.get_ticks()

        # State transition logic based on elapsed time
        if self.state == TrafficLightState.RED and current_time - self.timer >= self.red_duration:
            self.state = TrafficLightState.GREEN
            self.state_color = pygame.Color("green")
            self.timer = current_time  # Reset timer for the next state
        elif self.state == TrafficLightState.GREEN and current_time - self.timer >= self.green_duration:
            self.state = TrafficLightState.YELLOW
            self.state_color = pygame.Color("yellow")
            self.timer = current_time
        elif self.state == TrafficLightState.YELLOW and current_time - self.timer >= self.yellow_duration:
            self.state = TrafficLightState.RED
            self.state_color = pygame.Color("red")
            self.timer = current_time

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.circle(screen, self.state_color, (self.position.x, self.position.y), 10)
