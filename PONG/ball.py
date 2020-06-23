'''
title: the ball bounce between
'''

import pygame, sys
from window import Window
from sprite import Sprite
import random
from random import randrange
from player import Player1, Player2

class Ball(Sprite):

    def __init__(self, window, x=0, y=0):
        Sprite.__init__(self, window)
        self.setDimensions(30, 30)
        self.setPOS(self.window.getWidth()/2 - self.width/2, self.window.getHeight()/2 - self.height/2)
        self.sprite.fill(self.color)
        self.spdx = 10
        self.spdy = 10

    def move(self):
        self.x += self.spdx
        self.y += self.spdy

        # hit right bounder out of bounce player1 win
        if self.x > self.window.getWidth() - self.sprite.get_rect().width:
            self.x = self.window.getWidth() - self.sprite.get_rect().width
            self.spdx = (self.spdx) * -1

        # hit left bounder out of bounce player 2 win
        elif self.x < 0:
            self.x = 0
            self.spdx = (self.spdx) * -1

        # hit upper bounce bounce back
        if self.y > self.window.getHeight() - self.sprite.get_rect().height:
            self.y = self.window.getHeight() - self.sprite.get_rect().height
            self.spdy = (self.spdy) * -1

        # hit lower bounce bounce back
        elif self.y < 0:
            self.y = 0
            self.spdy = (self.spdy) * -1

        self.pos = (self.x, self.y)

    def collision1(self, player):
        if self.x < 65 and self.y > player.getY() and self.y + 30 < player.getY() + 120:
            self.x = 65
            self.spdx = (self.spdx) * -1
        else:
            pass

        self.pos = (self.x, self.y)

    def collision2(self, player):
        if self.x + 30 > 735 and self.y > player.getY() and self.y + 30 < player.getY() + 120:
            self.x = 705
            self.spdx = (self.spdx) * -1
        else:
            pass

        self.pos = (self.x, self.y)

if __name__ == "__main__":
    from pygame import init
    from window import Window

    init()
    window = Window()
    ball = Ball(window)

    while True:
        ball.move()
        window.getEvents()
        window.clearScreen()
        window.blitSprite(ball)
        window.updateScreen()
