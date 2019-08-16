#!/usr/bin/env python3

import time

import ledshim


ledshim.set_clear_on_exit()

light = 0

def set_lights(light):
    for i in range(7):
        pixel = (i * 4) + light
        if light == 0:
            ledshim.set_pixel(pixel, 255, 0, 0)
        elif light == 1:
            ledshim.set_pixel(pixel, 0, 255, 0)
        elif light == 2:
            ledshim.set_pixel(pixel, 0, 0, 255)
        elif light == 3:
            ledshim.set_pixel(pixel, 255, 255, 255)


try:
    while True:
        ledshim.clear()
        set_lights(light)
        ledshim.show()
        light = (light + 1) % 4
        time.sleep(1)
except KeyboardInterrupt:
    ledshim.clear()
    ledshim.show()
