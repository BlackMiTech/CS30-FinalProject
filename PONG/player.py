'''
title: the platform player controls
'''
from sprite import Sprite
from pygame import K_a, K_d, K_LEFT, K_RIGHT

class Player1(Sprite):

    def __init__(self, window, x = 0, y = 0):
        Sprite.__init__(self, window)
        self.setDimensions(15, 120)
        self.setPOS(50, self.window.getHeight()/2 - self.height/2)
        self.sprite.fill(self.rcolor)
        self.spd = 10

    def move(self, keys):
        if keys[K_a] == 1:
            self.y -= self.spd
        elif keys[K_d] == 1:
            self.y += self.spd

        if self.x > self.window.getWidth() - self.sprite.get_rect().width:
            self.x = self.window.getWidth() - self.sprite.get_rect().width
        elif self.x < 0:
            self.x = 0

        if self.y > self.window.getHeight() - self.sprite.get_rect().height:
            self.y = self.window.getHeight() - self.sprite.get_rect().height
        elif self.y < 0:
            self.y = 0

        self.pos = (self.x, self.y)

class Player2(Sprite):

    def __init__(self, window, x = 0, y = 0):
        Sprite.__init__(self, window)
        self.setDimensions(15, 120)
        self.setPOS(735, self.window.getHeight()/2 - self.height/2)
        self.sprite.fill(self.bcolor)
        self.spd = 10

    def move(self, keys):
        if keys[K_LEFT] == 1:
            self.y -= self.spd
        elif keys[K_RIGHT] == 1:
            self.y += self.spd

        if self.x > self.window.getWidth() - self.sprite.get_rect().width:
            self.x = self.window.getWidth() - self.sprite.get_rect().width
        elif self.x < 0:
            self.x = 0

        if self.y > self.window.getHeight() - self.sprite.get_rect().height:
            self.y = self.window.getHeight() - self.sprite.get_rect().height
        elif self.y < 0:
            self.y = 0

        self.pos = (self.x, self.y)


if __name__ == "__main__":
    from pygame import init
    from window import Window

    init()
    window = Window()
    player1 = Player1(window)
    player2 = Player2(window)

    while True:
        window.getEvents()
        player1.move(window.getKeyPressed())
        player2.move(window.getKeyPressed())
        window.getEvents()
        window.clearScreen()
        window.blitSprite(player1)
        window.blitSprite(player2)
        window.updateScreen()
