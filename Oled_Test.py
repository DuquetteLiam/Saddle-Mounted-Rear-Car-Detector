# Simple program to get the OLED Screen working on the pi

from board import SCL, SDA
import time
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106 

serial = i2c(port = 1, address = 0x3C)

device = sh1106(serial, width = 128, height = 64)

device.clear()

draw.rectangle((0, 0, 127, 63), outline=255, fill=0)

time.sleep(5)
