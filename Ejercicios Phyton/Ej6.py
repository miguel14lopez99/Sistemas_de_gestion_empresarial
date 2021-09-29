print("Introduce un numero")
n = int(input())

sum = 0
i = 1
for i in range(1,n):
    for j in range(1,n):
        sum += i+j

print("El sumatorio es: %d" %sum)