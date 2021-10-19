cont = 0
caracter = ''
vocales = {'a', 'e', 'i', 'o', 'u'}

while (caracter != ' '):
    print("Type a char")
    caracter = input()[0]

    for vocal in vocales:
        if vocal == caracter:
            cont += 1

print("Have been written %d vocals" %cont)