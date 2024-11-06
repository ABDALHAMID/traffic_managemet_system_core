import pygame

from simulation.Enums import TargetExit
from simulation.Spowner import Spawner
from simulation.TrafficLight import TrafficLight, TrafficLightState
from simulation.positionChecker import PositionStartChecker, PositionEndChecker, PositionStopChecker, \
    PositionDirectionChecker

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class TrafficSimulation:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Roundabout Traffic Light Simulation")

        # Load the background image and scale it to the screen size
        self.background = pygame.image.load("C:/Users/ABDVO/OneDrive/Documents/GitHub/traffic_managemet_system_core/backgrounds/background.png").convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()
        self.running = True


        self.traffic_lights = {
            "bl" : TrafficLight((250, 390), TrafficLightState.GREEN), #bootem left
            "tl" : TrafficLight((280, 120), TrafficLightState.RED), #top left
            "br" : TrafficLight((500, 410), TrafficLightState.RED), #bootem right
            "tr" : TrafficLight((520, 155), TrafficLightState.GREEN), #top right
        }

        self.positionCheckes = {
            "start" : {
                "l": PositionStartChecker((-50, 350), (5, 5), 0),
                "t": PositionStartChecker((350, -50), (5, 5), 90),
                "b": PositionStartChecker((460, 650), (5, 5), 270),
                "r": PositionStartChecker((850, 230), (5, 5), 180),
            },
            "end": {
                "l": PositionEndChecker((798, 300), (2, 100)),
                "t": PositionEndChecker((300, 598), (100, 2)),
                "b": PositionEndChecker((410, 0), (100, 2)),
                "r": PositionEndChecker((1, 180), (2, 100)),
            },
            "stop": {
                "l": PositionStopChecker((300, 300), (3, 100), self.traffic_lights["bl"]),
                "t": PositionStopChecker((300, 180), (100, 3), self.traffic_lights["tl"]),
                "b": PositionStopChecker((410, 390), (100, 3), self.traffic_lights["br"]),
                "r": PositionStopChecker((500, 180), (3, 100), self.traffic_lights["tr"]),
            },
            "first exit direction": {
                "l": PositionDirectionChecker((320, 360), (5, 5), 0,  TargetExit.FIRST_EXIT),
                "t": PositionDirectionChecker((335, 200), (5, 5), 90, TargetExit.FIRST_EXIT),
                "b": PositionDirectionChecker((470, 370), (5, 5), 270, TargetExit.FIRST_EXIT),
                "r": PositionDirectionChecker((480, 220), (5, 5), 180, TargetExit.FIRST_EXIT),
            },
            "third exit direction":{
                "l": PositionDirectionChecker((350, 350), (5, 5), 0, TargetExit.THIRD_EXIT),
                "t": PositionDirectionChecker((350, 230), (5, 5), 90, TargetExit.THIRD_EXIT),
                "b": PositionDirectionChecker((460, 340), (5, 5), 270, TargetExit.THIRD_EXIT),
                "r": PositionDirectionChecker((450, 230), (5, 5), 180, TargetExit.THIRD_EXIT),
            }
        }

        self.cars = []
        spawn_positions = []
        for positionChecke in self.positionCheckes["start"].values():
            spawn_positions.append(positionChecke)

        self.spawner = Spawner(spawn_positions, self.cars, interval=1000000)


    def run(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.spawner.update(event)

            # Draw the background image on the screen
            self.screen.blit(self.background, (0, 0))

            for light in self.traffic_lights.values():
                light.update()
                light.draw(self.screen)

            for checker in self.positionCheckes.values():
                for subChecker in checker.values():
                    subChecker.draw(self.screen)
                    subChecker.check_collision_with_vehicles(self.cars)


            # Update and draw all sprites
            for car in self.cars:
                car.update(self.cars)
                car.draw(self.screen)


            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()

simulation = TrafficSimulation()
simulation.run()
