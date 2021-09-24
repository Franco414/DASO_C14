"""
Ejercicio 4.3. Escribir una función que reciba por parámetro una dimensión n, e imprima la matriz
identidad correspondiente a esa dimensión.
"""

def imprimir_matriz_identidad(dimension):
    elemento=0
    matriz=[]
    fila=[]
    for i in range(0,dimension):
        fila=[]
        for j in range(0,dimension):
            if i==j:
                elemento=1
            else:
                elemento=0
            fila.append(elemento)
        matriz.append(fila)
    for i in range(0,dimension):
        print(matriz[i])

n=int(input("Ingrese la dimension de la matriz ==>"))
imprimir_matriz_identidad(n)