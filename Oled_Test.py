# Simple program to get the OLED Screen working on the pi

from board import SCL, SDA
import time
import adafruit_ssd1306
import busio

i2c = busio.I2C(SCL, SDA)

display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(1)

display.show

time.sleep(1000)

display.fill(0)