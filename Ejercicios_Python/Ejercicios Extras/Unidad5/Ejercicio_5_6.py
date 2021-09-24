"""
Ejercicio 5.6. Potencias de dos.
a) Escribir una función es_potencia_de_dos que reciba como parámetro un número natural,
y devuelva True si el número es una potencia de 2, y False en caso contrario.
b) Escribir una función que, dados dos números naturales pasados como parámetros, devuelva la
suma de todas las potencias de 2 que hay en el rango formado por esos números (0 si no hay
ninguna potencia de 2 entre los dos). Utilizar la función es_potencia_de_dos, descripta en
el punto anterior.
"""
#a)
def es_potencia_de_dos(numero):
    ret = False
    count=1
    while(count<=numero):
        if(numero==count):
            ret=True
        count=count*2
    return ret
"""
x = int(input("Ingrese un número ==> "))

if(es_potencia_de_dos(x)):
    print("El número %d es potencia de 2"%x)
else:
    print("El número %d no es potencia de 2"%x)
"""


#b)
def obt_suma_user(a,b):
    suma=0
    for i in range(a,b+1):
        if es_potencia_de_dos(i):
            suma=suma+i
    return suma

a = int(input("Ingrese un número ==> "))
b = int(input("Ingrese un número ==> "))
res=obt_suma_user(a,b)
print("La suma de las potencias de dos entre los numeros a y b es de ==> ",res)