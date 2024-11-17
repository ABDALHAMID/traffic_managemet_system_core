from simulation.Prefabs.Road import Road
from simulation.Prefabs.TrafficLight import TrafficLightState
from simulation.simulationStatics.PositionUtils import PositionUtils
from simulation.simulationSystemBack.SimulationObject import SimulationObject


class RoundAbout(SimulationObject):
    def __init__(self, position, size, direction, round_length):
        super().__init__(position, size, direction, (55,55,55,255))

        self.roads = {
            "l": Road(PositionUtils.getRelativeCenterLeftPositionToSize(self.position, self.direction, self.size,
                                                                        (round_length / 2, self.size.height / 4)),
                                                                        (round_length, self.size.height / 2),
                                                                        0 + self.direction.direction,
                                                                        TrafficLightState.GREEN),
            "t": Road(PositionUtils.getRelativeCenterLeftPositionToSize(self.position, self.direction, self.size,
                                                                        (round_length / 2, self.size.height / 4)),
                                                                        (round_length, self.size.height / 2),
                                                                        90 + self.direction.direction,
                                                                        TrafficLightState.GREEN),
            "r": Road(PositionUtils.getRelativeCenterLeftPositionToSize(self.position, self.direction, self.size,
                                                                        (round_length / 2, self.size.height / 4)),
                                                                        (round_length, self.size.height / 2),
                                                                        180 + self.direction.direction,
                                                                        TrafficLightState.GREEN),
            "b": Road(PositionUtils.getRelativeCenterLeftPositionToSize(self.position, self.direction, self.size,
                                                                        (round_length / 2, self.size.height / 4)),
                                                                        (round_length, self.size.height / 2),
                                                                        270 + self.direction.direction,
                                                                        TrafficLightState.GREEN),
        }