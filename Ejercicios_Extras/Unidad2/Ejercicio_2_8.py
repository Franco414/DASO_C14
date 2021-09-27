"""
Ejercicio 2.8. Modificar el programa anterior para que pueda generar fichas de un juego que puede tener
números de 0 a n.
"""
n=int(input("Ingrese el número n:"))
while(n<0 or n>100):
    print("El número ingresado es invalido")
    n=int(input("Ingrese el número n:"))
for i in range(0,n+1):
    for j in range(i,n+1):
        print(" %d | %d"%(i,j))