from logic import getState
from display import displayState, initializeDisplay
from detection import detect

initializeDisplay()

detection = []

while True:
    detection = detect()
    if detection[0] == "car":
        displayState(BEHIND)

