num = float(input("Type a number (type 100 to finish): "))
sum = 0
cont = 0

while num != 100:
    sum += num
    cont += 1
    num = float(input("Type a number (type 100 to finish): "))
    
avg = sum/cont

print("The average is: %d" %avg)
