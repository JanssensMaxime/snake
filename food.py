import pygame
import random


class Food():

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

    def get_rect(self):
        return self.rect

    #drawing food
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    #create random position for food
    def create_food(self):
       w = 500
       position = True
       x = random.randrange(20, w-20, 20)
       y = random.randrange(20, w-20, 20)
       self.rect = (x, y, self.width, self.height)