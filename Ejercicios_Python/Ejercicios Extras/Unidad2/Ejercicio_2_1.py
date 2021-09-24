"""
Ejercicio 2.1. Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés
y un número de años y muestre como resultado el monto final a obtener. La fórmula a utilizar es:
C n = C × (1 + x/100) n
Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.
"""
c =int(input("Ingrese el monto a invertir:"))
x =float(input("Ingresar una tasa de interes anual:"))
n =int(input("Ingresar un número de años n: "))

aux=1+x/100
res = c*aux*n
print("El capital a los {0} años sera de ==> ${1}".format(n,res))