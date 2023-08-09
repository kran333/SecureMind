# declaring the function name as ftok which accepts one parameyter as degrees_f
def ftok(degrees_f):
    # coverting the degree temp to kelvin
    # converting the interer value of degrees_f param in to float type
    result = 5/9*(float(degrees_f) + 459.67)
    # returing the result
    return result

print(ftok(32))