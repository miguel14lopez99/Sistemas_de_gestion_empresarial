num = int(input("Type a number: "))

cont = 0
for i in range(2,num):
    if num % i == 0:
        cont += 1      

if cont > 0 :
    print("%d isn't a prime number" %num)
else: 
    print("%d is a prime number" %num)