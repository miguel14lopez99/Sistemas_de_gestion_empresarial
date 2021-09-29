cont = 0
caracter = ''
vocales = {'a', 'e', 'i', 'o', 'u'}

while (caracter != ' '):
    print("Introduce un caracter")
    caracter = input()[0]

    for vocal in vocales:
        if vocal == caracter:
            cont += 1

print("Se han escrito %d vocales" %cont)