anio = int(input("Type a year: "))

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
    print("The year %d is leap" %anio)
else: 
    print("The year %d isn't leap" %anio)