#!/usr/bin/env python

# MIT License
# Original code: https://github.com/pimoroni/button-shim

import signal
import buttonshim
import requests

print("""
Button SHIM: rainbow.py

Light up the LED a different colour of the rainbow with each button pressed.

Press Ctrl+C to exit.

""")

@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    buttonshim.set_pixel(0x94, 0x00, 0xd3)
    try:
        r = requests.post('http://led-service/display/a', timeout=3)
        r = requests.post('http://inky-service/display/a', timeout=3)
    except requests.exceptions.RequestException as e:
        print e

@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    buttonshim.set_pixel(0x00, 0x00, 0xff)
    try:
        r = requests.post('http://led-service/display/b', timeout=3)
        r = requests.post('http://inky-service/display/b', timeout=3)
    except requests.exceptions.RequestException as e:
        print e

@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    buttonshim.set_pixel(0x00, 0xff, 0x00)
    try:
        r = requests.post('http://led-service/display/c', timeout=3)
        r = requests.post('http://inky-service/display/c', timeout=3)
    except requests.exceptions.RequestException as e:
        print e

@buttonshim.on_press(buttonshim.BUTTON_D)
def button_d(button, pressed):
    buttonshim.set_pixel(0xff, 0xff, 0x00)
    try:
        r = requests.post('http://led-service/display/d', timeout=3)
        r = requests.post('http://inky-service/display/d', timeout=3)
    except requests.exceptions.RequestException as e:
        print e

@buttonshim.on_press(buttonshim.BUTTON_E)
def button_e(button, pressed):
    buttonshim.set_pixel(0xff, 0x00, 0x00)
    try:
        r = requests.post('http://led-service/display/e', timeout=3)
        r = requests.post('http://inky-service/display/e', timeout=3)
    except requests.exceptions.RequestException as e:
        print e

signal.pause()