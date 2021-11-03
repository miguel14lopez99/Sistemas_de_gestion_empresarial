cont = 0
caracter = '' # i have to initialize this variable for the while statement
vocales = {'a', 'e', 'i', 'o', 'u'}

while (caracter != ' '): # while the inserted character is not equal to ' ' the program continues to run
    print("Type a char: ")
    caracter = input()[0]

    for vocal in vocales:
        if vocal == caracter:
            cont += 1

print("Have been written %d vocals" %cont)