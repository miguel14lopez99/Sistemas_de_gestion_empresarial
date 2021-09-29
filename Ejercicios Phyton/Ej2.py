print("Introduce un año")
anio = int(input())

def esBisiesto(anio):
    bisiesto = False

    print(anio+1)

    if (anio % 4) == 0 :
        bisiesto = True

    if ((anio % 100) == 0) and ((anio % 400) == 0) :
        bisiesto = True
    else:
        bisiesto = False
       
    return bisiesto

if(esBisiesto(anio)):
    print("El año %d es Bisiesto" %anio)
else: 
    print("El año %d no es Bisiesto" %anio)