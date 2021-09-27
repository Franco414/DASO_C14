"""
Ejercicio 2.6. Escribir un programa para tome una cantidad m de valores ingresados por el usuario, a
cada uno le calcule el factorial e imprima el resultado junto con el número de orden correspondiente.
"""

def encontrar_factorial(numero):
    factorial = 1
    for i in range(1,numero+1):
        factorial=factorial*i
    return factorial

n=int(input("ingrese la cantidad de numeros que desea ingresar: "))

for i in range(0,n):
    x = int(input("Ingrese un número"))
    while(x>20):
        x=int(input("Número muy elevado para hallar su factorial. Ingrese otro número"))
    fac=encontrar_factorial(x)
    print("El número ingresado es %d y su factorial es %d"%(x,fac))