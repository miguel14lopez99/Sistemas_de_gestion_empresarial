anio = int(input("Type a year: "))

def esBisiesto(anio):
    bisiesto = False

    print(anio+1)

    if (anio % 4) == 0 : #if the year is divisible by 4 is leap
        bisiesto = True

    if ((anio % 100) == 0) and ((anio % 400) == 0) : #if the year is divisible by 100 and 400 is leap
        bisiesto = True
    else:
        bisiesto = False
       
    return bisiesto

if(esBisiesto(anio)):
    print("The year %d is leap" %anio)
else: 
    print("The year %d isn't leap" %anio)