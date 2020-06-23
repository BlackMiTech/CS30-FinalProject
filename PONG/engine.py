'''
title: engine that put things together
'''

from window import Window
from player import *
from ball import Ball
from text import Text
from sprite import Sprite
import pygame

class Engine:
    def __init__(self):
        self.window = Window()
        self.player1 = Player1(self.window)
        self.player2 = Player2(self.window)
        self.ball = Ball(self.window)
        self.intro = Text("PONG 2.0", self.window)
        self.intro1 = Text("Player1: key a for up, key d for down.", self.window)
        self.intro2 = Text("Player2: key left for up, key right for down", self.window)
        self.intro3 = Text("Press Space to continue", self.window)
        self.title = Text("PONG 2.0", self.window)
        self.score = Text("Score: ", self.window)
        self.running = True

    def conti(self, keys):
        if keys[K_SPACE] == 1:
            self.running = True
        else:
            pass

    def run(self):
        while self.running:
            # --- INPUTS --- #
            self.window.getEvents()

            # --- PROCESSING --- #
            self.player1.move(self.window.getKeyPressed())
            self.player1.conti(self.window.getKeyPressed())
            self.player2.move(self.window.getKeyPressed())
            self.ball.move()
            self.ball.collision1(self.player1)
            self.ball.collision2(self.player2)
            self.score.setPOS(0, 20)
            self.intro.setPOS(150, 100)
            self.intro1.setPOS(150, 200)
            self.intro2.setPOS(150, 230)
            self.intro3.setPOS(150, 260)
            # --- OUTPUTS --- #

            self.window.clearScreen()
            self.window.blitSprite(self.intro)
            self.window.blitSprite(self.intro1)
            self.window.blitSprite(self.intro2)
            self.window.blitSprite(self.intro3)
            self.window.updateScreen()
            #  self.window.clearScreen()
            while self.player1.getcon() == True:
            #while self.running:
                self.window.clearScreen()
                # --- INPUTS --- #
                self.window.getEvents()

                # --- PROCESSING --- #
                self.player1.move(self.window.getKeyPressed())
                self.player1.conti(self.window.getKeyPressed())
                self.player2.move(self.window.getKeyPressed())
                self.ball.move()
                self.ball.collision1(self.player1)
                self.ball.collision2(self.player2)
                self.score.setPOS(0, 20)
                #self.intro1.setPOS(150, 200)
                #self.intro2.setPOS(150, 230)
                #self.intro3.setPOS(150, 260)
                # --- OUTPUTS --- #
                '''
                self.window.clearScreen()
                self.window.blitSprite(self.intro1)
                self.window.blitSprite(self.intro2)
                self.window.blitSprite(self.intro3)
                self.window.updateScreen()
                self.window.clearScreen()
                '''
                #if self.player1.getcon() == True:
                self.window.clearScreen()
                self.window.blitSprite(self.title)
                self.window.blitSprite(self.score)
                self.window.blitSprite(self.player1)
                self.window.blitSprite(self.player2)
                self.window.blitSprite(self.ball)
                self.window.updateScreen()


