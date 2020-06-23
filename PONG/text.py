'''
title: Text Sprites
'''

from sprite import Sprite
from loader import *
from pygame import font

class Text(Sprite):

    def __init__(self, content, window, x = 0, y = 0, fontFam = "Arial", fontSize = 24):
        Sprite.__init__(self, window, x, y)
        self.content = content
        self.fontFam = fontFam
        self.fontSize = fontSize
        self.color = WHITE
        self.font = font.SysFont(self.fontFam, self.fontSize)
        self.sprite = self.font.render(self.content, 1, self.color)

    # --- MODIFIER METHODS --- #

    def renderText(self):
        self.font = font.SysFont(self.fontFam, self.fontSize)
        self.sprite = self.font.render(self.content, 1, self.color)

    def setText(self, content):
        self.content = content
        self.renderText()

if __name__ == "__main__":
    from pygame import init
    from window import Window

    init()
    window = Window()
    text = Text("PONG 2.0", window)

    while True:
        window.getEvents()
        text.setText("PONG 2.0")
        window.clearScreen()
        window.blitSprite(text)
        window.updateScreen()


