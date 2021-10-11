num = int(input("Type a number: "))

sum = 0
for i in range(1,num):
    if num % i == 0:
        sum += i

if (sum > num):
    print("%d is an abundant number" %num)
else: 
    print("%d isn't an abundant number" %num)