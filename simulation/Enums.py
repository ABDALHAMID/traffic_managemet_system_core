from enum import Enum


class TargetExit(Enum):
    FIRST_EXIT = 90
    SECOND_EXIT = 0
    THIRD_EXIT = -90

class RoadAttributes(Enum):
    HASTRAFFICLIGHT = 1
    CANSPOWN = 1