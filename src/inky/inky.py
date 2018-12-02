#!/usr/bin/env python

# MIT License
# Original code: https://github.com/pimoroni/inky-phat

import sys
from PIL import ImageFont
from flask import Flask
import inkyphat

print("""Inky pHAT: Hello... my name is:
Use Inky pHAT as a personalised name badge!
""")

#inkyphat.set_rotation(180)

app = Flask(__name__)

@app.route("/health")
def health():
    print "Healthcheck"
    return "OK"

@app.route("/display/<name>", methods=['POST'])
def display(name):
    print "Received an update"
    update(name)
    return "OK"

app.run(host="0.0.0.0")

def update(name="k8s", colour="yellow"):
    try:
        inkyphat.set_colour(colour)
    except ValueError:
        print('Invalid colour "{}" for V{}\n'.format(colour, inkyphat.get_version()))
        if inkyphat.get_version() == 2:
            print(USAGE)
            sys.exit(1)
        print('Defaulting to "red"')

    # Show the backdrop image

    inkyphat.set_border(inkyphat.RED)
    inkyphat.set_image("resources/hello-badge.png")

    # Partial update if using Inky pHAT display v1

    if inkyphat.get_version() == 1:
        inkyphat.show()

    # Add the text

    font = ImageFont.truetype(inkyphat.fonts.AmaticSCBold, 38)

    w, h = font.getsize(name)

    # Center the text and align it with the name strip

    x = (inkyphat.WIDTH / 2) - (w / 2)
    y = 71 - (h / 2)

    inkyphat.text((x, y), name, inkyphat.BLACK, font)

    # Partial update if using Inky pHAT display v1

    if inkyphat.get_version() == 1:
        inkyphat.set_partial_mode(56, 96, 0, inkyphat.WIDTH)

    inkyphat.show()