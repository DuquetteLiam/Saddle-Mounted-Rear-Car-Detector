
#General Utilities
import time

#Oled Screen Utilities
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106 
from PIL import ImageFont






#Initializing OlED Display
serial = i2c(port = 1, address = 0x3C)
device = sh1106(serial, width = 128, height = 64)


def initializeDisplay():
    font = ImageFont.load_default()
    with canvas(device) as draw:
        draw.text((0, 0), "Rear Detector", font=font, fill=255)
        draw.text((0, 20), "System Ready", font=font, fill=255)
        time.sleep(2)

def displayState(state):
    if state == "No vehicle detected behind":
        with canvas(device) as draw:
            draw.text((0, 0), "No vehicle detected behind", font=font, fill=255)
            time.sleep(5)

    elif state == "Vehicle detected behind":
        with canvas(device) as draw:
            draw.text((0, 0), "Vehicle detected behind", font=font, fill=255)
            time.sleep(5)

    elif state == "Vehicle detected close behind":
        with canvas(device) as draw:
            draw.text((0, 0), "Vehicle detected close behind", font=font, fill=255)
            time.sleep(5)

    elif state == "Vehicle passed":
        with canvas(device) as draw:
            draw.text((0, 0), "Vehicle passed", font=font, fill=255)
            time.sleep(5)
            
