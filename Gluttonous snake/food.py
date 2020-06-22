'''
title: the food that the snake eat
'''

from window import Window
from player import Snake
from random import randrange

class Foods:

    def __init__(self):
        self.window = Window()
        self.foods = []
        for i in range(randrange(1, 5)):
            self.foods.append(Snake(self.window))
        for food in self.foods:
            food.setDimensions(30, 30)
            food.setPOS(randrange(self.window.getWidth()-food.getWidth()), randrange(self.window.getHeight()-food.getHeight()))

    def run(self):
        while True:
            # --- INPUTS
            self.window.getEvents()

            # --- PROCESS

            # --- OUTPUT
            self.window.clearScreen()
            for food in self.foods:
                self.window.blitSprite(food)
            self.window.updateScreen()

if __name__ == "__main__":
    from pygame import init
    init()
    food = Foods()
    food.run()