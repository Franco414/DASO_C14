"""
Ejercicio 2.5. Escribir un programa que reciba un número n por parámetro e imprima los primeros n
números triangulares, junto con su índice. Los números triangulares se obtienen mediante la suma de los
números naturales desde 1 hasta n. Es decir, si se piden los primeros 5 números triangulares, el programa
debe imprimir:
1 - 1
2 - 3
3 - 6
4 - 10
5 - 15
Nota: hacerlo usando y sin usar la ecuación
sumatoria desde i=1 hasta n
= n ∗ (n + 1)/2. ¿Cuál realiza más operaciones?
"""
n=int(input("Ingrese la cantidad de números triangulares que desea obtener:"))
print("Tabla de numeros triangulares")
print("   indice   ||   número triangular")
numero_triangular = 1
for i in range (1,n+1):
    numero_triangular = 0
    for j in range(1,i+1):
        numero_triangular=numero_triangular+j
    print("  %d  --   %d"%(i,numero_triangular))