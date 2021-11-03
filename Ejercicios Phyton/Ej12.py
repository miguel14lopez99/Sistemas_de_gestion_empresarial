num = int(input("Type a number: "))

cont = 0
for i in range(2,num): #from 2 to num the program checks if the number is divisible by any number if not is a prime number
    if num % i == 0:
        cont += 1      

if cont > 0 :
    print("%d isn't a prime number" %num)
else: 
    print("%d is a prime number" %num)