x = float(input("Type a number: "))

def approximate_square(num):
    cont = 0
    sqCont = cont**2

    while sqCont < num:
        cont += 1
        sqCont = cont**2

    cont -= 1
    return cont

n = approximate_square(x)

res = (n**4 + 6*(n**2)*x + x**2) / (4*(n**3) + 4*n*x)

print("The aproximated squared root of {} is {}".format(x, res))