
matrizA =   [[2,2,3,2,1],[3,3,2,1,2],[5,6,1,2,1],[1,2,2,2,3],[1,2,2,2,3]]
matrizRep = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
matrizOrd = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

dim = len(matrizA)

vector =[3,4,3,2,1,4,2,3,2,1] 

vectorCont = [0,0,0,0,0,0,0,0,0,0] # vector donde guardo la veces que se repiten en el vector los numeros del 0 al 9

# calcular cuantas veces se repite un numero en el vector (del 0 al 9)
for i in range(len(vector)):
    vectorCont[vector[i]] += 1

print("VectorCont2: ")
print(vectorCont)

# actualizar matrizRep

i = 0
j = 0

for k in range(dim*dim):
    matrizRep[i][j] = vectorCont[matrizA[i][j]]

    if ( j == dim-1 ):
        i += 1
        j = 0
    else:
        j += 1

print("Matriz de Repeticiones: ")
print(matrizRep)


# recorrer cada fila y ordenarla

def buscar_max(lista, ini, fin):
    pos_max = ini
    for i in range(ini+1, fin+1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

def ord_fila(fila):

    # n = posicion final de la fila, comienza en dim-1*
    n = dim-1

    # cicla mientras haya elementos para ordenar (2 o más elementos)
    while n > 0:
        # p es la posicion del mayor valor del segmento
        p = buscar_max(fila, 0, n)

        # intercambia el valor que está en p con el valor que
        # está en la última posición del segmento
        fila[p], fila[n] = fila[n], fila[p]

        n = n - 1
    return fila

for i in range(dim):
    matrizOrd[i] = ord_fila(matrizRep[i])

print("Matriz Ordenada: ")
print(matrizOrd)