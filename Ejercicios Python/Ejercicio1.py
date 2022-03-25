# se debe pedir por teclado
matrizA =   [[2,3,2,1],[6,5,4,2],[7,4,1,2],[1,3,1,2]]
matrizB =   [[2,3,2,1],[1,5,1,2],[3,4,1,2],[1,4,1,2]]

dim = len(matrizA)
elem = len(matrizA)*len(matrizA)

def producto_matrices(a, b, dim):
    filas_a = len(a)
    filas_b = len(b)
    columnas_a = len(a[0])
    columnas_b = len(b[0])

    res = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] # declaramos una matriz vacía de la misma dimensión

    # como se piden matrices cuadradas no hace falta comprobar si fila y columna son iguales

    # Rellenar el producto
    
    # for c in range(columnas_b):
    #     for i in range(filas_a):
    #         suma = 0
    #         for j in range(columnas_a):
    #             suma += a[i][j]*b[j][c]
    #         res[i][c] = suma
    # return res

    x=0
    y=0
    for z in range(dim):
        if z == dim:
            z=0
            y+=1
        if y == elem:
            y=0
            x+=1
        res[x][y] += matrizA[x][z] * matrizB[z][y]
    return res

res = producto_matrices(matrizA, matrizB, dim)

print(res)