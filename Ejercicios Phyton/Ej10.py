print("Type the minimum: ")
min = int(input())
print("Type the maximum: ")
max = int(input())

i = min
for i in range (min, max):
    if (i % 7) == 0:
        print("%d " %i)