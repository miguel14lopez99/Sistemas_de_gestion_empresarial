print("Introduce un mínimo")
min = int(input())
print("Introduce un máximo")
max = int(input())

i = min
for i in range (min, max):
    if (i % 7) == 0:
        print("%d " %i)