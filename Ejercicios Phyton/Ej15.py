num = int(input("Type a number: "))

sum = 1

def returnTheOdd(num):
    
    if(num % 2 == 0):
        oddNum = num-1
    else:
        oddNum = num

    return oddNum

num = returnTheOdd(num)

for i in range(num, 0, -2):
    sum *= i

print("The odd factorial is %d" %sum)