from typing import List


class DataCollector:
    def __init__(self, Simulation):
        self.Simulation = Simulation
        self.numberOfRoads: int
        self.carPerRoad: List[int]
        self.trafficLightsStatus: List[int]

    def collect(self):
        self.numberOfRoads = self.Simulation.getNumberOfRoads()
        #self.carPerRoad = self.Simulation.getCarPerRoad()
        self.trafficLightsStatus = self.Simulation.getTrafficLightsStatus()

    def update(self):
        self.collect()
        print(self.numberOfRoads)
        print(self.trafficLightsStatus)