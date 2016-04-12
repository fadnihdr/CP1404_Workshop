def calc_temp(tempCelcius):
    tempFahrenheit = (tempCelcius * 1.8) + 32
    print(tempFahrenheit)
    return tempFahrenheit

tempCelcius = float(input("What is the current temperature?(C)"))
calc_temp(tempCelcius)