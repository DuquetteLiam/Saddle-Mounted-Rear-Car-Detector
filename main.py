from logic import getState
from display import displayState, initializeDisplay

initializeDisplay()

while True:
    number = int(input("Enter a number: "))
    state = getState(number)
    displayState(state)
