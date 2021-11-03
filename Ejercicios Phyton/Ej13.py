num = int(input("Type a number: "))

sum = 0
for i in range(1,num): #from 2 to num the program checks if the number is divisible by any number
    if num % i == 0:
        sum += i       #sum those numbers

if (sum > num): # if the sum is greater than num, is an abundant number
    print("%d is an abundant number" %num) 
else: 
    print("%d isn't an abundant number" %num)