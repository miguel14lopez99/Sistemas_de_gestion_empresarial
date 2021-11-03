print("Type the amount of numbers: ")
n = int(input())

max = 0
i = 0
for i in range(0,n):
    print("Type the %dº" %(i+1))
    num = int(input())

    if max < num: # max updates if the program find a greater number
        max = num
    
print("The greatest is %d" %max)


