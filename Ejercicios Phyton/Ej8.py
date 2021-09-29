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
    print("Introduce un caracter")
    caracter = input()[0]

    if esVocal(caracter):
        contVocales += 1
    elif esConsonante(caracter):
        contConsonantes += 1
    else:
        contOtros += 1

print("Se han escrito %d vocales" %contVocales)
print("Se han escrito %d consonantes" %contConsonantes)
print("Se han escrito %d caracteres especiales" %contOtros)