

def getState(number):
    if number == 1:
        return("No Vehicle")

    elif number == 2:
        return("Vehicle detected behind")

    elif number == 3:
        return("Vehicle detected close behind")

    elif number == 4:
        return("Vehicle passed")

    else:
        return("invalid input")

