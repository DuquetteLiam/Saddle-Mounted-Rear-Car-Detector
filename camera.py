import time

from picamera2 import Picamera2
from picamera2.devices import IMX500


imx500 = IMX500("/path/to/rpk-file")
picam2 = Picamera2()
config = picam2.create_video_configuration()
picam2.start(config)
metadata = picam2.capture_metadata()
network_outputs = imx500.get_outputs(metadata)

time.sleep(5)

while True:
    print(network_outputs)
