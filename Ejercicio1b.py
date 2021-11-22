matrizA =   [[2,3,2,1],[6,5,4,2],[7,4,1,2],[1,3,1,2]]
matrizB =   [[2,3,2,1],[1,5,1,2],[3,4,1,2],[1,4,1,2]]

dim = len(matrizA)
elem = len(matrizA)*len(matrizA)

def producto_matrices(a, b, dim):

    res = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] # declaramos una matriz vacía de la misma dimensión

    # Rellenar el producto

    i=0
    j=0
    for k in range(dim*dim):
    
        res[i][j] += matrizA[i][j] * matrizB[i][j]

        if ( j == dim-1 ):
            i += 1
            j = 0
        else:
            j += 1

    return res

res = producto_matrices(matrizA, matrizB, dim)

print("Matriz de Resultado: ")
print(res)