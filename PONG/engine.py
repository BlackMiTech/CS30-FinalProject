'''
title: engine that put things together
'''

from window import Window
from player import Snake
from food import Food

import pygame

class Engine:
    def __init__(self):
        self.window = Window()
        self.player = Snake(self.window)
        self.food = Food(self.window)
        self.running = True

    def run(self):
        while self.running:
            # --- INPUTS --- #
            self.window.getEvents()

            # --- PROCESSING --- #
            self.player.move(self.window.getKeyPressed())
            self.food.getSpriteCollision(self.player)



            # --- OUTPUTS --- #
            self.window.clearScreen()
            self.window.blitSprite(self.player)
            self.window.blitSprite(self.food)
            if self.food.getco() == True:
                self.window.clearScreen()
                self.window.blitSprite(self.player)


            self.window.updateScreen()


