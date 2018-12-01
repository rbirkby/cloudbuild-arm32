#!/usr/bin/env python

import colorsys
import time
from flask import Flask
from sys import exit

try:
    import numpy as np
except ImportError:
    exit('This script requires the numpy module\nInstall with: sudo pip install numpy')

import ledshim

ledshim.set_clear_on_exit()

app = Flask(__name__)

@app.route("/health")
def health():
    print "Healthcheck"
    return "OK"

@app.route("/display/a", methods=['POST'])
def a():
    print "Received a update a"
    ledshim.set_all(128, 0, 0)
    ledshim.show()
    return "OK"

@app.route("/display/b", methods=['POST'])
def b():
    print "Received a update b"
    ledshim.set_all(0, 128, 0)
    ledshim.show()
    return "OK"

@app.route("/display/c", methods=['POST'])
def c():
    print "Received a update c"
    ledshim.set_all(0, 0, 128)
    ledshim.show()
    return "OK"

@app.route("/display/d", methods=['POST'])
def d():
    print "Received a update d"
    ledshim.set_all(128, 128, 0)
    ledshim.show()
    return "OK"

@app.route("/display/e", methods=['POST'])
def e():
    print "Received a update 3"
    ledshim.set_all(0, 128, 128)
    ledshim.show()
    return "OK"

def make_gaussian(fwhm):
    x = np.arange(0, ledshim.NUM_PIXELS, 1, float)
    y = x[:, np.newaxis]
    x0, y0 = 3.5, (ledshim.NUM_PIXELS / 2) - 0.5
    fwhm = fwhm
    gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
    return gauss


# while True:
#     for z in list(range(1, 10)[::-1]) + list(range(1, 10)):
#         fwhm = 15.0 / z
#         gauss = make_gaussian(fwhm)
#         start = time.time()
#         y = 4
#         for x in range(ledshim.NUM_PIXELS):
#             h = 0.5
#             s = 1.0
#             v = gauss[x, y]
#             rgb = colorsys.hsv_to_rgb(h, s, v)
#             r, g, b = [int(255.0 * i) for i in rgb]
#             ledshim.set_pixel(x, r, g, b)
#         ledshim.show()
#         end = time.time()
#         t = end - start
#         if t < 0.04:
#             time.sleep(0.04 - t)

if __name__ == '__main__':
    app.run()
