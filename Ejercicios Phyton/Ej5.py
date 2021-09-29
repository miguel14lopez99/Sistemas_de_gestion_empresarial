print("Introduce un numero")
n = int(input())

sum = 0
i = 1
for i in range(1,n):
    sum += pow(n+1,2)/(i+1)

print("El sumatorio es: %d" %sum)