#!/usr/bin/env python

# Unknown License
# Original code: https://github.com/pimoroni/vl53l1x-python

import os
import time
import sys
import signal
import requests
import VL53L1X

MAX_DISTANCE_MM = 800 # Distance at which our bar is full

print("""graph.py

Display a bar graph that ranges up to 80cm and turns yellow/red as the range decreases.

Press Ctrl+C to exit.

""")

"""
Open and start the VL53L1X ranging sensor
"""
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open() # Initialise the i2c bus and configure the sensor
tof.start_ranging(1) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range


running = True

def exit_handler(signal, frame):
    global running
    running = False
    tof.stop_ranging() # Stop ranging
    sys.stdout.write("\n")
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

while running:
    distance_in_mm = tof.get_distance() # Grab the range in mm
    distance_in_mm = min(MAX_DISTANCE_MM, distance_in_mm) # Cap at our MAX_DISTANCE

    try:
        r = requests.post('http://led-service/size/' + str(distance_in_mm), timeout=3)
    except requests.exceptions.RequestException as e:
        print e

    time.sleep(0.1)
