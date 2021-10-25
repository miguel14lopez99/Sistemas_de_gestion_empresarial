import math

degrees = float(input("Type the degrees: "))
rad = degrees * (math.pi/180)

def factorial(num):
    fact = 1
    for x in range(1,num+1):
        fact = fact * x
    return fact

def cos(rad):
    result = 0
    opt = 1
    for x in range(0,20,2):
        if opt == 1:
            result = result + (pow(rad, x)/factorial(x))
            opt = 2
        else:
            result = result - (pow(rad, x)/factorial(x))
            opt = 1

    return result

result = round(cos(rad),2)

print("The cos of {} is {}".format(degrees, result))
