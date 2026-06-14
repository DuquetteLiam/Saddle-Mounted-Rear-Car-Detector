# Simple program to get the OLED Screen working on the pi

from board import SCL, SDA
import time
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106 
from PIL import Image, ImageDraw, ImageFont, ImageText


#Initializing OlED Display
serial = i2c(port = 1, address = 0x3C)
device = sh1106(serial, width = 128, height = 64)

device.clear()

text = ImageText("Hello World")
image = Image.new("1", (128, 64), 0)
draw = ImageDraw.Draw(image)

draw.text((0, 0), text, fill=255)
device.display(text)

time.sleep(5)


