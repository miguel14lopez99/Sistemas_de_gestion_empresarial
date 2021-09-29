min = 0
print("Introduce un máximo")
max = int(input())

i = min
for i in range (min, max):
    if (i % 21) == 0:
        print("%d " %i)