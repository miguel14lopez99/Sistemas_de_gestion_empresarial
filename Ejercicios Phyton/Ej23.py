import math

number = float(input("Type the number: "))

def factorial(num):
    fact = 1
    for x in range(1,num+1):
        fact = fact * x
    return fact

def eToThePowerOf(num):
    res = 0
    for x in range(0,20):
            res = res + (pow(num, x)/factorial(x))
    return res

result = round(eToThePowerOf(number),2)

print("e to the power of {} is {}".format(number, result))