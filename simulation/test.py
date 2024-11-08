import pygame
from simulation.TrafficLight import TrafficLightState
from simulation.Road import Road  # Assuming Road is in simulation/Road.py

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Road Test")

# Define road parameters for testing
road_position = (400, 300)       # Center of the screen
road_size = (300, 100)            # Width and height of the road
road_direction = 140             # Direction in degrees
starting_traffic_light_state = TrafficLightState.GREEN  # Assuming TrafficLightState is an enum or similar
vehicles = []                    # Empty list for vehicles (for now)

# Create a Road instance
road = Road(position=road_position,
            size=road_size,
            direction=road_direction,
            startingStatus=starting_traffic_light_state,
            vehivles=vehicles)

# Main loop for testing the road display
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color
    screen.fill((50, 50, 50))

    # Draw the road on the screen
    road.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 30 FPS
    clock.tick(30)

# Quit Pygame
pygame.quit()
