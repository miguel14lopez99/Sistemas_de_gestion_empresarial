n = int(input("Type a number: "))

sum = 0
i = 1
for i in range(1,n):
    for j in range(1,n):
        sum += i+j

print("The summation is: %d" %sum)