#!/usr/bin/env python3

from random import randrange

from time import sleep

import ledshim


ledshim.set_clear_on_exit()

tick = 1
drops = []


class Drop:

    def __init__(self):
        self.falling = 0
        self.trail = randrange(3, 8)
        self.intensity_step = 255 / self.trail
        self.speed = randrange(1, 3)


    def fall(self, tick):
        if tick % self.speed == 0.0:
            self.falling += 1
            if self.falling > (28 + self.trail): self.falling = 0


def rain_drop(drop):
    intensity = 0
    for i in range(drop.trail, 0, -1):
        intensity += drop.intensity_step
        pixel = drop.falling - i
        if 0 <= pixel < 28:
            ledshim.set_pixel(pixel, 0, intensity, 0)

try:
    while True:
        if randrange(10) > 8:
            drops.append(Drop())
        ledshim.clear()
        for i in range(len(drops)):
            rain_drop(drops[i])
            drops[i].fall(tick)
        ledshim.show()
        drops = [drop for drop in drops if drop.falling != 0]
        tick += 1
        sleep(0.02)
except KeyboardInterrupt:
    ledshim.clear()
    ledshim.show()
