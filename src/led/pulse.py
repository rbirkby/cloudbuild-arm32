#!/usr/bin/env python

# MIT License
# Original code: https://github.com/pimoroni/led-shim

import colorsys
import time
from flask import Flask
from sys import exit
import threading

try:
    import numpy as np
except ImportError:
    exit('This script requires the numpy module\nInstall with: sudo pip install numpy')

import ledshim

ledshim.set_clear_on_exit()
lock = threading.Lock()
hue = 0.5
distance = 800
app = Flask(__name__)

@app.route("/health")
def health():
    print "Healthcheck"
    return "OK"

@app.route("/display/a", methods=['POST'])
def a():
    global hue
    print "Received a update a"
    with lock:
        hue = 0
    return "OK"

@app.route("/display/b", methods=['POST'])
def b():
    global hue
    print "Received a update b"
    with lock:
        hue = 0.2
    return "OK"

@app.route("/display/c", methods=['POST'])
def c():
    global hue
    print "Received a update c"
    with lock:
        hue = 0.4
    return "OK"

@app.route("/display/d", methods=['POST'])
def d():
    global hue
    print "Received a update d"
    with lock:
        hue = 0.6
    return "OK"

@app.route("/display/e", methods=['POST'])
def e():
    global hue
    print "Received a update e"
    with lock:
        hue = 0.8
    return "OK"

@app.route("/size/<int:newDistance>", methods=['POST'])
def size(newDistance):
    global distance
    print "Received a distance update" + str(newDistance)
    with lock:
        distance = newDistance
    return "OK"

def make_gaussian(fwhm):
    x = np.arange(0, ledshim.NUM_PIXELS, 1, float)
    y = x[:, np.newaxis]
    x0, y0 = 3.5, (ledshim.NUM_PIXELS / 2) - 0.5
    fwhm = fwhm
    gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
    return gauss

def pulse():
    while True:
        for z in list(range(1, 10)[::-1]) + list(range(1, 10)):
            fwhm = 15.0 / z
            gauss = make_gaussian(fwhm)
            start = time.time()
            y = 4
            with lock:
                for x in range(ledshim.NUM_PIXELS):
                    h = hue
                    s = 1.0 * (distance/float(800))
                    v = gauss[x, y]
                    rgb = colorsys.hsv_to_rgb(h, s, v)
                    r, g, b = [int(255.0 * i) for i in rgb]
                    ledshim.set_pixel(x, r, g, b)
                ledshim.show()
            end = time.time()
            t = end - start
            if t < 0.04:
                time.sleep(0.04 - t)

pulseThread = threading.Thread(name='pulseThread', target=pulse)
pulseThread.start()

app.run(host="0.0.0.0")
