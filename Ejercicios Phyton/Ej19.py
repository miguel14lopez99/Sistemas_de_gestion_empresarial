cont = 0

x = int(input("Type the dividend: "))
y = int(input("Type the divisor: "))

x -= y

while x >= 0 :
    cont += 1
    x -= y

print("The result is %d" %cont)