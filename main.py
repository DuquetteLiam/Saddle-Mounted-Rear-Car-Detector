from logic import getState
from display import displayState, initializeDisplay
from detection import detect, capture_result, initialize_detector

initializeDisplay()
initialize_detector()


while True:
    detection = detect(capture_result())
    if detection[0] == "car":
        displayState("BEHIND")

    else:
        displayState("NONE")

