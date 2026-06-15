from logic import getState
from display import displayState

while true:
    number = input("Enter a number")
    state = getState(number)
    displayState(state)
