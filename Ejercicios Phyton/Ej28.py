import math;
import cmath;

print("The formula to calculate the quadratic equation is:")
print("Ax^2 + Bx + C = 0\n")

a = int(input("Type the A number: \n"))
b = int(input("Type the B number: \n"))
c = int(input("Type the C number: \n"))

insideSqrt = b**2 - 4 * a * c

if insideSqrt >= 0:

    root1 = float(-b + math.sqrt(insideSqrt))/ (2 * a)
    root2 = float(-b - math.sqrt(insideSqrt))/ (2 * a)

elif insideSqrt < 0:

    root1 = (-b + cmath.sqrt(insideSqrt))/ (2 * a)
    root2 = (-b - cmath.sqrt(insideSqrt))/ (2 * a)

print('Solution:')
print(root1)
print(root2)