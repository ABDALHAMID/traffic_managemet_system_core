import math

from simulation.Prefabs.TrafficLight import TrafficLight, TrafficLightState
from simulation.Prefabs.positionChecker import PositionStopChecker, PositionStartChecker
from simulation.simulationStatics.PositionUtils import PositionUtils
from simulation.simulationSystemBack.SimulationObject import SimulationObject


class Road(SimulationObject):
    def __init__(self,
                 position: tuple[float, float],
                 size: tuple[float, float],
                 direction: float,
                 starting_status: TrafficLightState,
                 ):
        road_img = "C:/Users/ABDVO/OneDrive/Documents/GitHub/traffic_managemet_system_core/assets/images/roads/road.png"
        super().__init__(position, size, direction, road_img)

        traffic_light_x_offset = -30
        traffic_light_y_offset = 0

        traffic_light_position = PositionUtils.getRelativeBottomRightPositionToSize(self.position,
                                                                                    self.direction,
                                                                                    self.size,
                                                                                    (traffic_light_x_offset, traffic_light_y_offset))

        self.trafficLight = TrafficLight(traffic_light_position,
                                         self.direction.direction,
                                         starting_status)

        position_checker_x_offset = 0
        position_checker_y_offset = 0

        position_checker_position = PositionUtils.getRelativeCenterRightPositionToSize(self.position,
                                                                                       self.direction,
                                                                                       self.size,
                                                                                       (position_checker_x_offset,
                                                                          position_checker_y_offset))

        self.positionStopChecker = PositionStopChecker(position_checker_position,
                                                       (10, self.size.height),
                                                       self.direction.direction,
                                                       self.trafficLight)

        position_checker_x_offset = -50
        position_checker_y_offset = 0

        position_checker_position = PositionUtils.getRelativeCenterLeftPositionToSize(self.position,
                                                                                      self.direction,
                                                                                      self.size,
                                                                                      (position_checker_x_offset,
                                                                                        position_checker_y_offset))

        self.positionStartChecker = PositionStartChecker(position_checker_position,
                                                         (10, self.size.height),
                                                         self.direction.direction)

    def draw(self, screen):
        super().draw(screen)

        self.trafficLight.draw(screen)

        self.positionStopChecker.draw(screen)

        self.positionStartChecker.draw(screen)

    def update(self):
        pass

    def getStartChecker(self) -> PositionStartChecker:
        return self.positionStartChecker

    # def calcPos(self):
    #     position:(float, float)
    #     radian_angle = math.radians(self.direction)
    #     position[0] += math.cos(radian_angle)
    #     position[1] += math.sin(radian_angle)

