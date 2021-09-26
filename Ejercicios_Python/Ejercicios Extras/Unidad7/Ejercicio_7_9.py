"""
a) Escribir una función que reciba dos matrices y devuelva la suma.
b) Escribir una función que reciba dos matrices y devuelva el producto.
c) Escribir una función que opere sobre una matriz y mediante eliminación gaussiana devuelva una
matriz triangular superior.
d) Escribir una función que indique si un grupo de vectores, recibidos mediante una lista, son
linealmente independientes o no.
"""
#a)
def suma_matrices(matriz_A,matriz_B):
    matriz_C=[]
    lista=[]
    for i in range(0,len(matriz_A)):
        lista=[]
        for j in range(0,len(matriz_A[0])):
            aux=matriz_A[i][j]+matriz_B[i][j]
            lista.append(aux)
        matriz_C.append(lista)
    return matriz_C

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
c=suma_matrices(a,b)
for i in c:
    print(i)