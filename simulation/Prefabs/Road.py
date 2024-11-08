import math

from simulation.Prefabs.TrafficLight import TrafficLight, TrafficLightState
from simulation.Prefabs.positionChecker import PositionStopChecker
from simulation.simulationSystemBack.SimulationObject import SimulationObject


class Road(SimulationObject):
    def __init__(self,
                 position: tuple[float, float],
                 size: tuple[float, float],
                 direction: float,
                 starting_status: TrafficLightState,
                 vehivles,
                 ):
        road_img = "C:/Users/ABDVO/OneDrive/Documents/GitHub/traffic_managemet_system_core/assets/images/roads/road.png"
        super().__init__(position, size, direction, road_img)
        self.vehivles = vehivles

        traffic_light_x_offset = -30
        traffic_light_y_offset = 0
        bottom_right_x = (self.position.x +
                          math.cos(math.radians(self.direction.direction)) * (
                                      self.size.width / 2 + traffic_light_x_offset) -
                          math.sin(math.radians(self.direction.direction)) * (
                                      self.size.height / 2 + traffic_light_y_offset))

        bottom_right_y = (self.position.y +
                          math.sin(math.radians(self.direction.direction)) * (
                                      self.size.width / 2 + traffic_light_x_offset) +
                          math.cos(math.radians(self.direction.direction)) * (
                                      self.size.height / 2 + traffic_light_y_offset))

        self.trafficLight = TrafficLight( (bottom_right_x, bottom_right_y),
                                         self.direction.direction,
                                         starting_status)

        self.positionStopChecker = PositionStopChecker((self.position.x + math.cos(math.radians(self.direction.direction)) * self.size.width/2,
                                                        self.position.y + math.sin(math.radians(self.direction.direction)) * self.size.width/2),
                                                       (10, self.size.height),
                                                       self.trafficLight)

    def draw(self, screen):
        super().draw(screen)

        self.trafficLight.draw(screen)

        self.positionStopChecker.draw(screen, self.direction.direction)

    def update(self):
        pass

    # def calcPos(self):
    #     position:(float, float)
    #     radian_angle = math.radians(self.direction)
    #     position[0] += math.cos(radian_angle)
    #     position[1] += math.sin(radian_angle)

