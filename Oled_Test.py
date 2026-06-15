# Simple program to get the OLED Screen working on the pi


import time
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106 
from PIL import ImageFont


#Initializing OlED Display
serial = i2c(port = 1, address = 0x3C)
device = sh1106(serial, width = 128, height = 64)


font = ImageFont.load_default()
with canvas(device) as draw:
    draw.text((0, 0), "Rear Detector", font=font, fill=255)
    draw.text((0, 20), "System Ready", font=font, fill=255)

time.sleep(5)




