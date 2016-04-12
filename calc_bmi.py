def calbmi(weight,height):
    bmi =  weight / (height * height)
    print(bmi)
    return bmi

weight = float(input("How much do you weigh:"))
height = float(input("How tall are you:"))
calbmi(weight,height)
