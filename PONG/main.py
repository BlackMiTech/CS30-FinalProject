"""
title: PONG
Author: Zhihong Liang & Jimmy Wang
"""

from pygame import init
from engine import Engine

if __name__ == "__main__":
    init()
    game = Engine()
    game.run()