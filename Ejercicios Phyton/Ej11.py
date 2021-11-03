min = 0
print("Type the maximum: ")
max = int(input())

i = min
for i in range (min, max): # from 0 to max the program only prints those numbers that are divisible by 21
    if (i % 21) == 0:
        print("%d " %i)