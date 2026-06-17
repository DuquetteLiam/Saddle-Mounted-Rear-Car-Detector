import time

from picamera2 import Picamera2
from picamera2.devices import IMX500


imx500 = IMX500("/usr/share/imx500-models/imx500_network_nanodet_plus_416x416_pp.rpk")
picam2 = Picamera2()
config = picam2.create_video_configuration()
picam2.start(config)


time.sleep(5)

while True:
    metadata = picam2.capture_metadata()
    network_outputs = imx500.get_outputs(metadata)
    print("type: " + str(type(metadata)))
    print()
    print("metadata: " + str(metadata))


    print()
    print("type: " + str(type(network_outputs)))
    print("output: " + str(network_outputs))
    time.sleep(5)
