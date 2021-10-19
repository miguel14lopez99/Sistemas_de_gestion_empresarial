min = 0
print("Type the maximum: ")
max = int(input())

i = min
for i in range (min, max):
    if (i % 21) == 0:
        print("%d " %i)