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
        self.scorep1 = Text("Player1 Score: ", self.window)
        self.scorep2 = Text("Player2 Score: ", self.window)
        self.p1oint0 = Text("0", self.window)
        self.p1oint1 = Text("1", self.window)
        self.p1oint2 = Text("2", self.window)
        self.p1oint3 = Text("3", self.window)
        self.p1oint4 = Text("4", self.window)
        self.p1oint5 = Text("5", self.window)
        self.p1oint6 = Text("6", self.window)
        self.p1oint7 = Text("7", self.window)
        self.p1oint8 = Text("8", self.window)
        self.p1oint9 = Text("9", self.window)
        self.p1oint10 = Text("10", self.window)

        self.p2oint0 = Text("0", self.window)
        self.p2oint1 = Text("1", self.window)
        self.p2oint2 = Text("2", self.window)
        self.p2oint3 = Text("3", self.window)
        self.p2oint4 = Text("4", self.window)
        self.p2oint5 = Text("5", self.window)
        self.p2oint6 = Text("6", self.window)
        self.p2oint7 = Text("7", self.window)
        self.p2oint8 = Text("8", self.window)
        self.p2oint9 = Text("9", self.window)
        self.p2oint10 = Text("10", self.window)

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
            self.scorep1.setPOS(0, 30)
            self.scorep2.setPOS(600, 30)
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

            while self.player1.getcon() == True:
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
                self.scorep1.setPOS(0, 30)
                self.scorep2.setPOS(600, 30)
                if self.ball.getp1s() == 0:
                    self.p1oint0.setPOS(160, 30)
                    self.p1oint1.setPOS(-100, -100)
                    self.p1oint2.setPOS(-100, -100)
                    self.p1oint3.setPOS(-100, -100)
                    self.p1oint4.setPOS(-100, -100)
                    self.p1oint5.setPOS(-100, -100)
                    self.p1oint6.setPOS(-100, -100)
                    self.p1oint7.setPOS(-100, -100)
                    self.p1oint8.setPOS(-100, -100)
                    self.p1oint9.setPOS(-100, -100)
                    self.p1oint10.setPOS(-100, -100)
                elif self.ball.getp1s() == 1:
                    self.p1oint0.setPOS(-100, -100)
                    self.p1oint1.setPOS(160, 30)
                    self.p1oint2.setPOS(-1000, -100)
                    self.p1oint3.setPOS(-1000, -100)
                    self.p1oint4.setPOS(-100, -100)
                    self.p1oint5.setPOS(-100, -100)
                    self.p1oint6.setPOS(-100, -100)
                    self.p1oint7.setPOS(-100, -100)
                    self.p1oint8.setPOS(-100, -100)
                    self.p1oint9.setPOS(-100, -100)
                    self.p1oint10.setPOS(-100, -100)
                elif self.ball.getp1s() == 2:
                    self.p1oint0.setPOS(-100, -100)
                    self.p1oint1.setPOS(-100, -100)
                    self.p1oint2.setPOS(160, 30)
                    self.p1oint3.setPOS(-100, -100)
                    self.p1oint4.setPOS(-100, -100)
                    self.p1oint5.setPOS(-100, -100)
                    self.p1oint6.setPOS(-100, -100)
                    self.p1oint7.setPOS(-100, -100)
                    self.p1oint8.setPOS(-100, -100)
                    self.p1oint9.setPOS(-100, -100)
                    self.p1oint10.setPOS(-100, -100)
                elif self.ball.getp1s() == 3:
                    self.p1oint0.setPOS(-100, -100)
                    self.p1oint1.setPOS(-100, -100)
                    self.p1oint2.setPOS(-100, -100)
                    self.p1oint3.setPOS(160, 30)
                    self.p1oint4.setPOS(-100, -100)
                    self.p1oint5.setPOS(-100, -100)
                    self.p1oint6.setPOS(-100, -100)
                    self.p1oint7.setPOS(-100, -100)
                    self.p1oint8.setPOS(-100, -100)
                    self.p1oint9.setPOS(-100, -100)
                    self.p1oint10.setPOS(-100, -100)
                elif self.ball.getp1s() == 4:
                    self.p1oint0.setPOS(-100, -100)
                    self.p1oint1.setPOS(-100, -100)
                    self.p1oint2.setPOS(-100, -100)
                    self.p1oint3.setPOS(-100, -100)
                    self.p1oint4.setPOS(160, 30)
                    self.p1oint5.setPOS(-100, -100)
                    self.p1oint6.setPOS(-100, -100)
                    self.p1oint7.setPOS(-100, -100)
                    self.p1oint8.setPOS(-100, -100)
                    self.p1oint9.setPOS(-100, -100)
                    self.p1oint10.setPOS(-100, -100)
                elif self.ball.getp1s() == 5:
                    self.p1oint0.setPOS(-100, -100)
                    self.p1oint1.setPOS(-100, -100)
                    self.p1oint2.setPOS(-100, -100)
                    self.p1oint3.setPOS(-100, -100)
                    self.p1oint4.setPOS(-100, -100)
                    self.p1oint5.setPOS(160, 30)
                    self.p1oint6.setPOS(-100, -100)
                    self.p1oint7.setPOS(-100, -100)
                    self.p1oint8.setPOS(-100, -100)
                    self.p1oint9.setPOS(-100, -100)
                    self.p1oint10.setPOS(-100, -100)
                elif self.ball.getp1s() == 6:
                    self.p1oint0.setPOS(-100, -100)
                    self.p1oint1.setPOS(-100, -100)
                    self.p1oint2.setPOS(-100, -100)
                    self.p1oint3.setPOS(-100, -100)
                    self.p1oint4.setPOS(-100, -100)
                    self.p1oint5.setPOS(-100, -100)
                    self.p1oint6.setPOS(160, 30)
                    self.p1oint7.setPOS(-100, -100)
                    self.p1oint8.setPOS(-100, -100)
                    self.p1oint9.setPOS(-100, -100)
                    self.p1oint10.setPOS(-100, -100)
                elif self.ball.getp1s() == 7:
                    self.p1oint0.setPOS(-100, -100)
                    self.p1oint1.setPOS(-100, -100)
                    self.p1oint2.setPOS(-100, -100)
                    self.p1oint3.setPOS(-100, -100)
                    self.p1oint4.setPOS(-100, -100)
                    self.p1oint5.setPOS(-100, -100)
                    self.p1oint6.setPOS(-100, -100)
                    self.p1oint7.setPOS(160, 30)
                    self.p1oint8.setPOS(-100, -100)
                    self.p1oint9.setPOS(-100, -100)
                    self.p1oint10.setPOS(-100, -100)
                elif self.ball.getp1s() == 8:
                    self.p1oint0.setPOS(-100, -100)
                    self.p1oint1.setPOS(-100, -100)
                    self.p1oint2.setPOS(-100, -100)
                    self.p1oint3.setPOS(-100, -100)
                    self.p1oint4.setPOS(-100, -100)
                    self.p1oint5.setPOS(-100, -100)
                    self.p1oint6.setPOS(-100, -100)
                    self.p1oint7.setPOS(-100, -100)
                    self.p1oint8.setPOS(160, 30)
                    self.p1oint9.setPOS(-100, -100)
                    self.p1oint10.setPOS(-100, -100)
                elif self.ball.getp1s() == 9:
                    self.p1oint0.setPOS(-100, -100)
                    self.p1oint1.setPOS(-100, -100)
                    self.p1oint2.setPOS(-100, -100)
                    self.p1oint3.setPOS(-100, -100)
                    self.p1oint4.setPOS(-100, -100)
                    self.p1oint5.setPOS(-100, -100)
                    self.p1oint6.setPOS(-100, -100)
                    self.p1oint7.setPOS(-100, -100)
                    self.p1oint8.setPOS(-100, -100)
                    self.p1oint9.setPOS(160, 30)
                    self.p1oint10.setPOS(-100, -100)
                elif self.ball.getp1s() == 10:
                    self.p1oint0.setPOS(-100, -100)
                    self.p1oint1.setPOS(-100, -100)
                    self.p1oint2.setPOS(-100, -100)
                    self.p1oint3.setPOS(-100, -100)
                    self.p1oint4.setPOS(-100, -100)
                    self.p1oint5.setPOS(-100, -100)
                    self.p1oint6.setPOS(-100, -100)
                    self.p1oint7.setPOS(-100, -100)
                    self.p1oint8.setPOS(-100, -100)
                    self.p1oint9.setPOS(-100, -100)
                    self.p1oint10.setPOS(160, 30)

                if self.ball.getp2s() == 0:
                    self.p2oint0.setPOS(760, 30)
                    self.p2oint1.setPOS(-100, -100)
                    self.p2oint2.setPOS(-100, -100)
                    self.p2oint3.setPOS(-100, -100)
                    self.p2oint4.setPOS(-100, -100)
                    self.p2oint5.setPOS(-100, -100)
                    self.p2oint6.setPOS(-100, -100)
                    self.p2oint7.setPOS(-100, -100)
                    self.p2oint8.setPOS(-100, -100)
                    self.p2oint9.setPOS(-100, -100)
                    self.p2oint10.setPOS(-100, -100)
                elif self.ball.getp2s() == 1:
                    self.p2oint0.setPOS(-100, -100)
                    self.p2oint1.setPOS(760, 30)
                    self.p2oint2.setPOS(-100, -100)
                    self.p2oint3.setPOS(-100, -100)
                    self.p2oint4.setPOS(-100, -100)
                    self.p2oint5.setPOS(-100, -100)
                    self.p2oint6.setPOS(-100, -100)
                    self.p2oint7.setPOS(-100, -100)
                    self.p2oint8.setPOS(-100, -100)
                    self.p2oint9.setPOS(-100, -100)
                    self.p2oint10.setPOS(-100, -100)
                elif self.ball.getp2s() == 2:
                    self.p2oint0.setPOS(-100, -100)
                    self.p2oint1.setPOS(-100, -100)
                    self.p2oint2.setPOS(760, 30)
                    self.p2oint3.setPOS(-100, -100)
                    self.p2oint4.setPOS(-100, -100)
                    self.p2oint5.setPOS(-100, -100)
                    self.p2oint6.setPOS(-100, -100)
                    self.p2oint7.setPOS(-100, -100)
                    self.p2oint8.setPOS(-100, -100)
                    self.p2oint9.setPOS(-100, -100)
                    self.p2oint10.setPOS(-100, -100)
                elif self.ball.getp2s() == 3:
                    self.p2oint0.setPOS(-100, -100)
                    self.p2oint1.setPOS(-100, -100)
                    self.p2oint2.setPOS(-100, -100)
                    self.p2oint3.setPOS(760, 30)
                    self.p2oint4.setPOS(-100, -100)
                    self.p2oint5.setPOS(-100, -100)
                    self.p2oint6.setPOS(-100, -100)
                    self.p2oint7.setPOS(-100, -100)
                    self.p2oint8.setPOS(-100, -100)
                    self.p2oint9.setPOS(-100, -100)
                    self.p2oint10.setPOS(-100, -100)
                elif self.ball.getp2s() == 4:
                    self.p2oint0.setPOS(-100, -100)
                    self.p2oint1.setPOS(-100, -100)
                    self.p2oint2.setPOS(-100, -100)
                    self.p2oint3.setPOS(-100, -100)
                    self.p2oint4.setPOS(760, 30)
                    self.p2oint5.setPOS(-100, -100)
                    self.p2oint6.setPOS(-100, -100)
                    self.p2oint7.setPOS(-100, -100)
                    self.p2oint8.setPOS(-100, -100)
                    self.p2oint9.setPOS(-100, -100)
                    self.p2oint10.setPOS(-100, -100)
                elif self.ball.getp2s() == 5:
                    self.p2oint0.setPOS(-100, -100)
                    self.p2oint1.setPOS(-100, -100)
                    self.p2oint2.setPOS(-100, -100)
                    self.p2oint3.setPOS(-100, -100)
                    self.p2oint4.setPOS(-100, -100)
                    self.p2oint5.setPOS(760, 30)
                    self.p2oint6.setPOS(-100, -100)
                    self.p2oint7.setPOS(-100, -100)
                    self.p2oint8.setPOS(-100, -100)
                    self.p2oint9.setPOS(-100, -100)
                    self.p2oint10.setPOS(-100, -100)
                elif self.ball.getp2s() == 6:
                    self.p2oint0.setPOS(-100, -100)
                    self.p2oint1.setPOS(-100, -100)
                    self.p2oint2.setPOS(-100, -100)
                    self.p2oint3.setPOS(-100, -100)
                    self.p2oint4.setPOS(-100, -100)
                    self.p2oint5.setPOS(-100, -100)
                    self.p2oint6.setPOS(760, 30)
                    self.p2oint7.setPOS(-100, -100)
                    self.p2oint8.setPOS(-100, -100)
                    self.p2oint9.setPOS(-100, -100)
                    self.p2oint10.setPOS(-100, -100)
                elif self.ball.getp2s() == 7:
                    self.p2oint0.setPOS(-100, -100)
                    self.p2oint1.setPOS(-100, -100)
                    self.p2oint2.setPOS(-100, -100)
                    self.p2oint3.setPOS(-100, -100)
                    self.p2oint4.setPOS(-100, -100)
                    self.p2oint5.setPOS(-100, -100)
                    self.p2oint6.setPOS(-100, -100)
                    self.p2oint7.setPOS(760, 30)
                    self.p2oint8.setPOS(-100, -100)
                    self.p2oint9.setPOS(-100, -100)
                    self.p2oint10.setPOS(-100, -100)
                elif self.ball.getp2s() == 8:
                    self.p2oint0.setPOS(-100, -100)
                    self.p2oint1.setPOS(-100, -100)
                    self.p2oint2.setPOS(-100, -100)
                    self.p2oint3.setPOS(-100, -100)
                    self.p2oint4.setPOS(-100, -100)
                    self.p2oint5.setPOS(-100, -100)
                    self.p2oint6.setPOS(-100, -100)
                    self.p2oint7.setPOS(-100, -100)
                    self.p2oint8.setPOS(760, 30)
                    self.p2oint9.setPOS(-100, -100)
                    self.p2oint10.setPOS(-100, -100)
                elif self.ball.getp2s() == 9:
                    self.p2oint0.setPOS(-100, -100)
                    self.p2oint1.setPOS(-100, -100)
                    self.p2oint2.setPOS(-100, -100)
                    self.p2oint3.setPOS(-100, -100)
                    self.p2oint4.setPOS(-100, -100)
                    self.p2oint5.setPOS(-100, -100)
                    self.p2oint6.setPOS(-100, -100)
                    self.p2oint7.setPOS(-100, -100)
                    self.p2oint8.setPOS(-100, -100)
                    self.p2oint9.setPOS(760, 30)
                    self.p2oint10.setPOS(-100, -100)
                elif self.ball.getp2s() == 10:
                    self.p2oint0.setPOS(-100, -100)
                    self.p2oint1.setPOS(-100, -100)
                    self.p2oint2.setPOS(-100, -100)
                    self.p2oint3.setPOS(-100, -100)
                    self.p2oint4.setPOS(-100, -100)
                    self.p2oint5.setPOS(-100, -100)
                    self.p2oint6.setPOS(-100, -100)
                    self.p2oint7.setPOS(-100, -100)
                    self.p2oint8.setPOS(-100, -100)
                    self.p2oint9.setPOS(-100, -100)
                    self.p2oint10.setPOS(760, 30)

                # --- OUTPUTS --- #
                self.window.clearScreen()
                self.window.blitSprite(self.title)
                self.window.blitSprite(self.scorep1)
                self.window.blitSprite(self.scorep2)
                self.window.blitSprite(self.player1)
                self.window.blitSprite(self.player2)
                self.window.blitSprite(self.ball)
                # player 1 score
                self.window.blitSprite(self.p1oint0)
                self.window.blitSprite(self.p1oint1)
                self.window.blitSprite(self.p1oint2)
                self.window.blitSprite(self.p1oint3)
                self.window.blitSprite(self.p1oint4)
                self.window.blitSprite(self.p1oint5)
                self.window.blitSprite(self.p1oint6)
                self.window.blitSprite(self.p1oint7)
                self.window.blitSprite(self.p1oint8)
                self.window.blitSprite(self.p1oint9)
                self.window.blitSprite(self.p1oint10)
                # player 2 score
                self.window.blitSprite(self.p2oint0)
                self.window.blitSprite(self.p2oint1)
                self.window.blitSprite(self.p2oint2)
                self.window.blitSprite(self.p2oint3)
                self.window.blitSprite(self.p2oint4)
                self.window.blitSprite(self.p2oint5)
                self.window.blitSprite(self.p2oint6)
                self.window.blitSprite(self.p2oint7)
                self.window.blitSprite(self.p2oint8)
                self.window.blitSprite(self.p2oint9)
                self.window.blitSprite(self.p2oint10)
                self.window.updateScreen()


