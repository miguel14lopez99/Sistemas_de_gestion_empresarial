m1 = int(input("Type the first mass: "))
m2 = int(input("Type the second mass: "))
r = int(input("Type the distance: "))

g = 6.67e-11

f = g*(m1*m2)/(pow(r,2))

print("The gravitatory force between {}kg and {}kg throught {}m is {}N".format(m1, m2, r, f))