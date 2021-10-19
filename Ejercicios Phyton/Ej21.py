amount = int(input("Type the amount of characters: "))
c = input("Type the character to be counted: ")[0]
cont = 0

for x in range(amount):
    char = input("Type the %dº char: " %(x+1))[0]

    if char == c: 
        cont += 1

print("The character '{}' has been found {} times".format(c, cont))
