from abc import ABC

import pygame


class Position:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value: float):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value: float):
        self.__y = value


class Size:
    def __init__(self, width: float, height: float):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value: float):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value: float):
        self.__height = value


class Direction:
    def __init__(self, direction: float):
        self.__direction = direction % 360

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        self.__direction = value % 360


class GameObject(ABC):
    def __init__(self, position: tuple[float, float], size: tuple[float, float], direction: float):
        if len(position) != 2:
            raise ValueError("Position must be a tuple of two values (x, y).")
        self.position = Position(position[0], position[1])

        if len(size) != 2:
            raise ValueError("Size must be a tuple of two values (x, y).")
        self.size = Size(size[0], size[1])

        self.direction = Direction(direction)


class SimulationObject(GameObject, ABC):
    def __init__(self,
                 position: tuple[float, float],
                 size: tuple[float, float],
                 direction: float,
                 color: tuple[int, int, int, int] | str):
        super().__init__(position=position,size=size,direction=direction)
        self.color = color


    def draw(self, screen):

        print(self.color)
        if isinstance(self.color, tuple) and len(self.color) == 4 and all(isinstance(c, int) for c in self.color):
            self.__draw_surface(screen, self.color)
        elif isinstance(self.color, str):
            self.__draw_image(screen, self.color)
        else:
            raise ValueError("Color must be either a tuple of four integers (RGBA) or a string")

    def __draw_surface(self, screen, color: tuple[int, int, int, int]):
        size = (self.size.width, self.size.height)
        position = (self.position.x, self.position.y)
        surface = pygame.Surface(size, pygame.SRCALPHA)
        color = pygame.Color(color)
        surface.fill(color)
        rotated_surface = pygame.transform.rotate(surface, -self.direction.direction)
        rotated_rect = rotated_surface.get_rect(center=position)
        screen.blit(rotated_surface, rotated_rect.topleft)

    def __draw_image(self, screen, image_path: str):
        size = (self.size.width, self.size.height)
        position = (self.position.x, self.position.y)
        original_image = pygame.image.load(image_path).convert_alpha()
        original_image = pygame.transform.scale(original_image, size)
        image = pygame.transform.rotate(original_image, -self.direction.direction)
        rect = image.get_rect(center=position)
        screen.blit(image, rect)
