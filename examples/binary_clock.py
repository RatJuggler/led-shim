#!/usr/bin/env python

from time import localtime, sleep

import ledshim

ledshim.set_clear_on_exit()

# 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
# ||                         ||                         ||
# Red (hours)                ||                         ||
#       32 16 08 04 02 01    ||                         ||
#                            Green (minutes)            ||
#                                  32 16 08 04 02 01    ||
#                                                       Blue (seconds)
#                                                             32 16 08 04 02 01

while True:
    t = localtime()
    h, m, s = t.tm_hour, t.tm_min, t.tm_sec

    ledshim.clear()

    ledshim.set_pixel(0, 255, 0, 0)
    for x in range(6):
        bit = (h & (1 << x)) > 0
        r, g, b = [128 * bit] * 3
        ledshim.set_pixel(7 - x, r, g, b)

    ledshim.set_pixel(9, 0, 255, 0)
    for x in range(6):
        bit = (m & (1 << x)) > 0
        r, g, b = [128 * bit] * 3
        ledshim.set_pixel(16 - x, r, g, b)

    ledshim.set_pixel(18, 0, 0, 255)
    for x in range(6):
        bit = (s & (1 << x)) > 0
        r, g, b = [128 * bit] * 3
        ledshim.set_pixel(25 - x, r, g, b)

    ledshim.show()
    print('{h:2d}:{m:02d}:{s:02d}'.format(h=h, m=m, s=s))

    sleep(1)
