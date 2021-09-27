"""
Ejercicio 1.4. Implementar algoritmos que resuelvan los siguientes problemas:
a) Dados dos números, indicar la suma, resta, división y multiplicación de ambos.
b) Dado un número entero N, imprimir su tabla de multiplicar.
c) Dado un número entero N, imprimir su factorial.
"""
#a)
def operaciones_1(a,b):
    print("Suma de {0} y {1} ==> {0} + {1} = {2}".format(a,b,a+b))
    print("Resta de {0} con {1} ==> {0} - {1} = {2}".format(a,b,a-b))
    print("Division entera entre {0} y {1} ==> {0} : {1} = {2}".format(a,b,a//b))
    print("Division real entre {0} y {1} ==> {0} : {1} = {2}".format(a,b,a/b))
    print("Multiplicacion entre {0} y {1} ==> {0} x {1} = {2}".format(a,b,a*b))
#b)
def obtener_tabla_mult(numero):
    print("tabla de multiplicar del numero %d"%numero)
    for i in range(0,10):
        print("{0} x {1} = {2}".format(numero,i,numero*i))
    return
#c)
def encontrar_factorial(numero):
    factorial = 1
    for i in range(1,numero+1):
        factorial=factorial*i
    return factorial

operaciones_1(4,5)
obtener_tabla_mult(13)
print( "el factorial del numero es",encontrar_factorial(3))