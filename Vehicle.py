import pygame
import random



class Vehicle:
    def __init__(self, start_pos, speed = 1):
        self.position = pygame.Vector2(start_pos)
        self.widht = 40
        self.height = 40
        self.speed = speed
        self.color = pygame.Color("red")
        self.stopped = False

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position.x, self.position.y, self.widht, self.height))

    def move(self):
        self.position += self.speed
