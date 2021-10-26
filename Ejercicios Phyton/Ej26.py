num = int(input("Type a number (from 0 to 10): "))

while num < 0 or num > 10:
    num = int(input("Error. Type a number (from 0 to 10): "))

print("The multiplication table of {} is: ".format(num))
for x in range(11):
    print("{} x {} = {}".format(num, x, (num*x)))