contVocales = 0
contConsonantes = 0
contOtros = -1
caracter = ''
vocales = {'a','e','i','o','u'}
consonantes = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'}

def esVocal(caracter):
    a = False

    for vocal in vocales:
        if vocal == caracter:
            a = True
    
    return a

def esConsonante(caracter):
    b = False

    for consonante in consonantes:
        if consonante == caracter:
            b = True
    
    return b

while (caracter != ' '):
    print("Type a char: ")
    caracter = input()[0]

    if esVocal(caracter):
        contVocales += 1
    elif esConsonante(caracter):
        contConsonantes += 1
    else:
        contOtros += 1

print("Have been written %d vocals" %contVocales)
print("Have been written %d consonants" %contConsonantes)
print("Have been written %d special characters" %contOtros)