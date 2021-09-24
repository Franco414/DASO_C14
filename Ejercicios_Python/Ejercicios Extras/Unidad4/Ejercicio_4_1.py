"""
Ejercicio 4.1. Escribir funciones que resuelvan los siguientes problemas:
a) Dado un número entero n, indicar si es o no par.
b) Dado un número entero n, indicar si es o no primo.
"""

def es_par(numero):
    return (numero%2) == 0

def es_primo(numero):
    resultado=True
    if numero>=-1 and numero<=1:
        return resultado
    for i in range(2,numero):
        if numero%i==0:
            resultado=False
            break
    return resultado

x = int(input("Ingrese un número"))
if es_par(x):
    print("el numero %d, es par"%x)
else:
    print("el numero %d, es impar"%x)

y = int(input("Ingrese un número"))
if es_primo(y):
    print("el numero %d, es primo"%y)
else:
    print("el numero %d, no es primo"%y)