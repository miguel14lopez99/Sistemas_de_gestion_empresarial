num = int(input("Type a number (type 100 to finish): "))
sum = 0
cont = 0

while num > 0:
    sum += num
    cont += 1
    num = int(input("Type a number (type 100 to finish): "))
    
avg = sum/cont

print("The average is: %d" %avg)