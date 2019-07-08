#!/usr/bin/env python

# Random blinks using the ANU Quantum Random Numbers Server, see http://qrng.anu.edu.au

import ledshim, requests, json
from time import sleep

ledshim.set_clear_on_exit()

while True:
    response = requests.get("https://qrng.anu.edu.au/API/jsonI.php?type=hex16&length=28&size=3",  timeout=3)
    if response.status_code == 200:
        anu_json = json.loads(response.text)
        data = anu_json["data"]
        for i in range(ledshim.NUM_PIXELS):
            pixel = bytearray.fromhex(data[i])
            print(pixel[0], pixel[1], pixel[2])
            ledshim.set_pixel(i, pixel[0], pixel[1], pixel[2])
        ledshim.show()
    print("Blink!")
    sleep(1)
