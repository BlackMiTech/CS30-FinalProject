'''
title: the snake player controls
'''
from sprite import Sprite
from pygame import K_s, K_d, K_a, K_w

class Snake(Sprite):

    def __init__(self, window, x = 0, y = 0):
        Sprite.__init__(self, window)
        self.setDimensions(50, 50)
        self.setPOS(self.window.getWidth()/2 - self.width/2, self.window.getHeight()/2 - self.height/2)
        self.spd = 10

    def move(self, keys):
        if keys[K_d] == 1:
            self.x += self.spd
        elif keys[K_a] == 1:
            self.x -= self.spd
        if keys[K_w] == 1:
            self.y -= self.spd
        elif keys[K_s] == 1:
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
    snake = Snake(window)

    while True:
        window.getEvents()
        snake.move(window.getKeyPressed())
        window.getEvents()
        window.clearScreen()
        window.blitSprite(snake)
        window.updateScreen()
