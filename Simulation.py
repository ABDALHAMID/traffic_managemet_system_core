import pygame
from Vehicle import Vehicle

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class TrafficSimulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Roundabout Traffic Light Simulation")

        # Load the background image and scale it to the screen size
        self.background = pygame.image.load("./backgrounds/background.png").convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()
        self.running = True

        # Create the vehicle sprite with a custom size
        self.car1 = Vehicle(start_pos=(-50, 350), speed=2, direction=0, image_path="./cars/red_car.png", size=(50, 25))
        self.all_sprites = pygame.sprite.Group(self.car1)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Draw the background image on the screen
            self.screen.blit(self.background, (0, 0))

            # Update and draw all sprites
            self.all_sprites.update()
            self.car1.turn(0)  # Optional: Control turning speed
            self.all_sprites.draw(self.screen)

            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()

# Create and run the simulation
simulation = TrafficSimulation()
simulation.run()
