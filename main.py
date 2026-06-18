from logic import getState
from display import displayState, initializeDisplay
from detection import detect, capture_result

initializeDisplay()


while True:
    detection = detect(capture_result())
    if detection[0] == "car":
        displayState(BEHIND)

