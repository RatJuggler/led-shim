#!/usr/bin/env python3

import random
import time

import ledshim


ledshim.set_clear_on_exit()


def pumpkin():
    for i in range(5):
        ledshim.set_pixel(i, 69, 229, 33)
    for i in range(5, ledshim.NUM_PIXELS):
        ledshim.set_pixel(i, 255, 145, 0)
    ledshim.show()
    time.sleep(3 + random.randint(1, 5))


def dark():
    ledshim.clear()
    ledshim.show()
    time.sleep(random.randint(1, 4))


def lightning():
    ledshim.clear()
    for i in range(0, ledshim.NUM_PIXELS - 2, 3):
        ledshim.set_pixel(i, 255, 255, 255)
        ledshim.set_pixel(i + 1, 255, 255, 255)
        ledshim.set_pixel(i + 2, 255, 255, 255)
        ledshim.show()
    for i in range(0, ledshim.NUM_PIXELS - 2, 3):
        ledshim.set_pixel(i, 0, 0, 0)
        ledshim.set_pixel(i + 1, 0, 0, 0)
        ledshim.set_pixel(i + 2, 0, 0, 0)
        ledshim.show()


def ghost():
    ledshim.clear()
    position = 0
    for i in range(random.randint(ledshim.NUM_PIXELS * 2, ledshim.NUM_PIXELS * 4)):
        ledshim.clear()
        for g in range(position, position + 4, 2):
            ledshim.set_pixel(g, 255, 255, 255)
            ledshim.set_pixel(g + 1, 255, 255, 255)
        ledshim.show()
        if position < ledshim.NUM_PIXELS // 4 or (random.randint(1, 2) == 1 and position < ledshim.NUM_PIXELS // 4 * 3):
            position += 2
        elif position > ledshim.NUM_PIXELS // 4:
            position -= 2
    for i in range(position, ledshim.NUM_PIXELS - 4, 2):
        ledshim.clear()
        for g in range(i, i + 4, 2):
            ledshim.set_pixel(g, 255, 255, 255)
            ledshim.set_pixel(g + 1, 255, 255, 255)
        ledshim.show()


def spider():
    ledshim.clear()
    drop = ledshim.NUM_PIXELS // 4 + random.randint(1, ledshim.NUM_PIXELS // 2)
    for i in range(0, drop):
        ledshim.set_pixel(i, 100, 100, 100)
        ledshim.set_pixel(i + 1, 101, 147, 245)
        ledshim.set_pixel(i + 2, 101, 147, 245)
        ledshim.show()
    time.sleep(random.randint(1, 5))
    for i in range(drop, 0, -1):
        ledshim.set_pixel(i, 101, 147, 245)
        ledshim.set_pixel(i + 1, 101, 147, 245)
        ledshim.set_pixel(i + 2, 0, 0, 0)
        ledshim.show()


try:
    while True:
        effect = random.randint(1, 4)
        if effect == 1:
            pumpkin()
        elif effect == 2:
            lightning()
        elif effect == 3:
            ghost()
        elif effect == 4:
            spider()
        dark()
except KeyboardInterrupt:
    ledshim.clear()
    ledshim.show()
