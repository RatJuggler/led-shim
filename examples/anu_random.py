#!/usr/bin/env python

# Random blinks using the ANU Quantum Random Numbers Server, see http://qrng.anu.edu.au

import ledshim, requests, json
from time import sleep


def get_random_numbers():
    try:
        response = requests.get("https://qrng.anu.edu.au/API/jsonI.php?type=hex16&length=28&size=3",  timeout=3)
        response.raise_for_status()
        anu_json = json.loads(response.text)
        return anu_json["data"]
    except requests.exceptions.RequestException:
        return


def render_pixels():
    for i in range(ledshim.NUM_PIXELS):
        pixel = bytearray.fromhex(data[i])
        print(pixel[0], pixel[1], pixel[2])
        ledshim.set_pixel(i, pixel[0], pixel[1], pixel[2])


ledshim.set_clear_on_exit()

while True:
    data = get_random_numbers()
    if data is None:
        ledshim.clear()
    else:
        render_pixels()
        ledshim.show()
    print("Blink!")
    sleep(1)
