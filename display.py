
#General Utilities
import time

#Oled Screen Utilities
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106 
#Display Utilities
from PIL import ImageFont


#OlED Display Settings
serial = i2c(port = 1, address = 0x3C)
device = sh1106(serial, width = 128, height = 64)


#font = ImageFont.load_default()

font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    16
)

#Make sure the display works
def initializeDisplay():
    with canvas(device) as draw:
        draw.text((0, 0), "Detector", font=font, fill=255)
        draw.text((0, 20), "System Ready", font=font, fill=255)
    time.sleep(2)

def displayState(state):
    if state == "NONE":
        with canvas(device) as draw:
            draw.text((0, 0), "No Vehicle", font=font, fill=255)
        

    elif state == "BEHIND":
        with canvas(device) as draw:
            draw.text((0, 0), "Vehicle Behind", font=font, fill=255)
        

    elif state == "CLOSE":
        with canvas(device) as draw:
            draw.text((0, 0), "Vehicle Close", font=font, fill=255)
        

    elif state == "PASSED":
        with canvas(device) as draw:
            draw.text((0, 0), "Vehicle Passed", font=font, fill=255)

    else:
        with canvas(device) as draw:
            draw.text((0, 0), "State Error", font=font, fill=255)

    time.sleep(0.25)
        
            
