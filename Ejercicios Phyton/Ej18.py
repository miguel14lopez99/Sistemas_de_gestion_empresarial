while True:
    amount = int(input("Type the amount of numbers: "))
    sum = 0

    for x in range(amount):
        num = int(input("Type the %dº number: " %(x+1)))
        sum += num

    avg = sum/amount
    print("The average is %d \n" %avg)