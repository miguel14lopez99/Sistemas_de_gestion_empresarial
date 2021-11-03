print("Type the minimum: ")
min = int(input())
print("Type the maximum: ")
max = int(input())

i = min
for i in range (min, max): # from min to max the program only prints those numbers that are divisible by 7
    if (i % 7) == 0:
        print("%d " %i)