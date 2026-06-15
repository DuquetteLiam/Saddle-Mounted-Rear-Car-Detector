

def getState(number):
    if number == 1:
        return("No vehicle detected behind")

    elif number == 2:
        return("Vehicle detected behind")

    elif number == 3:
        return("Vehicle detected close behind")

    elif number == 4:
        return("vehicle passed")

    else:
        return("invalid input")

