'''
title: engine that put things together
'''

from window import Window
from player import *
from ball import Ball

import pygame

class Engine:
    def __init__(self):
        self.window = Window()
        self.player1 = Player1(self.window)
        self.player2 = Player2(self.window)
        self.ball = Ball(self.window)
        self.running = True

    def run(self):
        while self.running:
            # --- INPUTS --- #
            self.window.getEvents()

            # --- PROCESSING --- #
            self.player1.move(self.window.getKeyPressed())
            self.player2.move(self.window.getKeyPressed())
            self.ball.move()
            self.ball.collision1(self.player1)
            self.ball.collision2(self.player2)
            # --- OUTPUTS --- #
            self.window.clearScreen()
            self.window.blitSprite(self.player1)
            self.window.blitSprite(self.player2)
            self.window.blitSprite(self.ball)

            self.window.updateScreen()


