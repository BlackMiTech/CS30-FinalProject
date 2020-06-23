'''
title: the food that the snake eat
'''

import pygame, sys
from window import Window
from sprite import Sprite
from random import randrange
from player import Snake
class Food(Sprite):

    def __init__(self, window, x=0, y=0):
        Sprite.__init__(self, window)
        self.setDimensions(30, 30)
        self.setPOS(randrange(1, 800), randrange(1, 600))
        self.sprite.fill(self.rcolor)


if __name__ == "__main__":
    from pygame import init
    from window import Window

    init()
    window = Window()
    food = Food(window)

    while True:
        window.getEvents()
        window.getEvents()
        window.clearScreen()
        window.blitSprite(food)
        window.updateScreen()
