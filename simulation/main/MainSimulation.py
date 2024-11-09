import time

import pygame

from simulation.Prefabs.Road import Road
from simulation.Prefabs.TrafficLight import TrafficLightState
from simulation.Spowner import Spawner

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class TrafficSimulation:
    def __init__(self):
        self.seconds = None
        self.minutes = None
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Roundabout Traffic Light Simulation")

        # Load the background image and scale it to the screen size
        self.background = pygame.image.load("C:/Users/ABDVO/OneDrive/Documents/GitHub/traffic_managemet_system_core/backgrounds/background.png").convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()
        self.start_time = time.time()
        self.running = True

        # self.dataCollector = DataCollector(self)


        # self.traffic_lights: Dict[str, TrafficLight] = {
        #     "l" : TrafficLight((250, 390), TrafficLightState.GREEN), #bootem left
        #     "t" : TrafficLight((280, 120), TrafficLightState.RED), #top left
        #     "b" : TrafficLight((500, 410), TrafficLightState.RED), #bootem right
        #     "r" : TrafficLight((520, 155), TrafficLightState.GREEN), #top right
        # }

        # self.positionCheckes = {
        #     "start" : {
        #         "l": PositionStartChecker((-50, 350), (5, 5), 0),
        #         "t": PositionStartChecker((350, -50), (5, 5), 90),
        #         "b": PositionStartChecker((460, 650), (5, 5), 270),
        #         "r": PositionStartChecker((850, 230), (5, 5), 180),
        #     },
        #     "end": {
        #         "l": PositionEndChecker((798, 300), (2, 100)),
        #         "t": PositionEndChecker((300, 598), (100, 2)),
        #         "b": PositionEndChecker((410, 0), (100, 2)),
        #         "r": PositionEndChecker((1, 180), (2, 100)),
        #     },
        #     "stop": {
        #         "l": PositionStopChecker((300, 300), (3, 100), self.traffic_lights["l"]),
        #         "t": PositionStopChecker((300, 180), (100, 3), self.traffic_lights["t"]),
        #         "b": PositionStopChecker((410, 390), (100, 3), self.traffic_lights["b"]),
        #         "r": PositionStopChecker((500, 180), (3, 100), self.traffic_lights["r"]),
        #     },
        #     "first exit direction": {
        #         "l": PositionDirectionChecker((330, 360), (5, 5), 0,  TargetExit.FIRST_EXIT),
        #         "t": PositionDirectionChecker((335, 220), (5, 5), 90, TargetExit.FIRST_EXIT),
        #         "b": PositionDirectionChecker((470, 350), (5, 5), 270, TargetExit.FIRST_EXIT),
        #         "r": PositionDirectionChecker((460, 220), (5, 5), 180, TargetExit.FIRST_EXIT),
        #     },
        #     "third exit direction":{
        #         "l": PositionDirectionChecker((460, 340), (5, 5), 0, TargetExit.THIRD_EXIT),
        #         "t": PositionDirectionChecker((350, 330), (5, 5), 90, TargetExit.THIRD_EXIT),
        #         "b": PositionDirectionChecker((450, 230), (5, 5), 270, TargetExit.THIRD_EXIT),
        #         "r": PositionDirectionChecker((360, 230), (5, 5), 180, TargetExit.THIRD_EXIT),
        #     }
        # }

        self.roads = {
            "l" : Road((150, 300), (300, 100), 0, TrafficLightState.GREEN),
            "t": Road((400, 150), (300, 100), 90, TrafficLightState.GREEN),
            "r": Road((650, 300), (300, 100), 180, TrafficLightState.GREEN),
            "b": Road((400, 450), (300, 100), 270, TrafficLightState.GREEN),
        }

        self.cars = []
        spawn_positions = []
        for positionChecke in self.roads.values():
            spawn_positions.append(positionChecke.getStartChecker())

        self.spawner = Spawner(spawn_positions, self.cars, interval=1500)

        self.text_vechule_spowned : pygame.font.Font
        self.text_vechule_destroyed : pygame.font.Font

    def update_text(self):
        font = pygame.font.Font(None, 25)
        self.text_vechule_spowned = font.render(f"number of vehicles spawned: {Spawner.totalVehicles}", True,(100, 100, 255))
        self.text_vechule_destroyed = font.render(f"number of vehicles destroyed: {PositionEndChecker.carFinishedCount}",True, (100, 255, 100))

    def draw_elapsed_time(self):
        font = pygame.font.Font(None, 20)
        elapsed_time = time.time() - self.start_time
        self.minutes = int(elapsed_time // 60)
        self.seconds = int(elapsed_time % 60)
        time_text = font.render(f"Time elapsed: {self.minutes:02}:{self.seconds:02}", True, (255, 255, 255))
        self.screen.blit(time_text, (10, 90))

    def run(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(f"number of vehicles spawned: {Spawner.totalVehicles}")
                    # print(f"number of vehicles destroyed: {PositionEndChecker.carFinishedCount}")
                    print(f"Time elapsed: {self.minutes:02}:{self.seconds:02}")
                    self.running = False
                self.spawner.update(event)

            # self.update_text()
            # Draw the background image on the screen
            self.screen.blit(self.background, (0, 0))
            # self.screen.blit(self.text_vechule_spowned, (10, 10))
            # self.screen.blit(self.text_vechule_destroyed, (10, 50))

            self.draw_elapsed_time()

            for road in self.roads.values():
                road.update()
                road.draw(self.screen)

            self.spawner.update()


            # Update and draw all sprites
            for car in self.cars:
                car.update(self.cars)
                car.draw(self.screen)


            # self.dataCollector.update()

            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()

    def getNumberOfRoads(self):
        return self.traffic_lights.__len__()

    def getTrafficLightsStatus(self):
        states: list[TrafficLightState] = [light.state for light in self.traffic_lights.values()]
        return states

    def getCarsPerRoad(self):
        pass


simulation = TrafficSimulation()
simulation.run()
