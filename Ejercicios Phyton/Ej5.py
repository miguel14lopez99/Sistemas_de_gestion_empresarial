n = int(input("Type a number: "))

sum = 0
i = 1
for i in range(1,n):
    sum += pow(n+1,2)/(i+1)

print("The summation is: %d" %sum)