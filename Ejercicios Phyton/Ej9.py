print("Introduce la cantidad de numeros")
n = int(input())

max = 0
i = 0
for i in range(0,n):
    print("Introduce el %dº" %(i+1))
    num = int(input())

    if max < num:
        max = num
    
print("El mayor es el %d" %max)


