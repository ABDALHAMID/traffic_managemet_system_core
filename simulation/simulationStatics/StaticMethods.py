import math

from simulation.simulationSystemBack.SimulationObject import Position, Size, Direction


class StaticMethods:
    @staticmethod
    def getRelativeBottomRightPositionToSize(position: Position,
                                             direction: Direction,
                                             size: Size,
                                             offset: tuple[float, float]) \
            -> tuple[float, float]:
        bottom_right_x = (position.x +
                          math.cos(math.radians(direction.direction)) * (size.width / 2 + offset[0]) -
                          math.sin(math.radians(direction.direction)) * (size.height / 2 + offset[1]))

        bottom_right_y = (position.y +
                          math.sin(math.radians(direction.direction)) * (size.width / 2 + offset[0]) +
                          math.cos(math.radians(direction.direction)) * (size.height / 2 + offset[1]))

        new_position = (bottom_right_x, bottom_right_y)
        return new_position

    @staticmethod
    def getRelativeTopRightPositionToSize(position: Position,
                                          direction: Direction,
                                          size: Size,
                                          offset: tuple[float, float]) \
            -> tuple[float, float]:
        top_right_x = (position.x +
                       math.cos(math.radians(direction.direction)) * (size.width / 2 + offset[0]) +
                       math.sin(math.radians(direction.direction)) * (size.height / 2 + offset[1]))

        top_right_y = (position.y +
                       math.sin(math.radians(direction.direction)) * (size.width / 2 + offset[0]) -
                       math.cos(math.radians(direction.direction)) * (size.height / 2 + offset[1]))

        new_position = (top_right_x, top_right_y)
        return new_position

    @staticmethod
    def getRelativeTopLeftPositionToSize(position: Position,
                                         direction: Direction,
                                         size: Size,
                                         offset: tuple[float, float]) \
            -> tuple[float, float]:
        top_left_x = (position.x -
                      math.cos(math.radians(direction.direction)) * (size.width / 2 - offset[0]) +
                      math.sin(math.radians(direction.direction)) * (size.height / 2 - offset[1]))

        top_left_y = (position.y -
                      math.sin(math.radians(direction.direction)) * (size.width / 2 - offset[0]) -
                      math.cos(math.radians(direction.direction)) * (size.height / 2 - offset[1]))

        new_position = (top_left_x, top_left_y)
        return new_position

    @staticmethod
    def getRelativeBottomLeftPositionToSize(position: Position,
                                            direction: Direction,
                                            size: Size,
                                            offset: tuple[float, float]) \
            -> tuple[float, float]:
        bottom_left_x = (position.x -
                         math.cos(math.radians(direction.direction)) * (size.width / 2 - offset[0]) -
                         math.sin(math.radians(direction.direction)) * (size.height / 2 - offset[1]))

        bottom_left_y = (position.y -
                         math.sin(math.radians(direction.direction)) * (size.width / 2 - offset[0]) +
                         math.cos(math.radians(direction.direction)) * (size.height / 2 - offset[1]))

        new_position = (bottom_left_x, bottom_left_y)
        return new_position

    @staticmethod
    def getRelativeCenterPositionToSize(position: Position,
                                        direction: Direction,
                                        size: Size,
                                        offset: tuple[float, float]) \
            -> tuple[float, float]:
        center_x = position.x + offset[0]
        center_y = position.y + offset[1]

        new_position = (center_x, center_y)
        return new_position

    @staticmethod
    def getRelativeCenterRightPositionToSize(position: Position,
                                             direction: Direction,
                                             size: Size,
                                             offset: tuple[float, float]) \
            -> tuple[float, float]:
        center_right_x = (position.x +
                          math.cos(math.radians(direction.direction)) * (size.width / 2 + offset[0]))

        center_right_y = (position.y +
                          math.sin(math.radians(direction.direction)) * (size.width / 2 + offset[0]))

        new_position = (center_right_x, center_right_y)
        return new_position

    @staticmethod
    def getRelativeCenterLeftPositionToSize(position: Position,
                                            direction: Direction,
                                            size: Size,
                                            offset: tuple[float, float]) \
            -> tuple[float, float]:
        center_left_x = (position.x -
                         math.cos(math.radians(direction.direction)) * (size.width / 2 - offset[0]))

        center_left_y = (position.y -
                         math.sin(math.radians(direction.direction)) * (size.width / 2 - offset[0]))

        new_position = (center_left_x, center_left_y)
        return new_position
