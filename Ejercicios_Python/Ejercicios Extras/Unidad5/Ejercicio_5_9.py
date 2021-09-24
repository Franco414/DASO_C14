"""
Ejercicio 5.9. Escribir una función que reciba dos números como parámetros, y devuelva cuántos múl-
tiplos del primero hay, que sean menores que el segundo.
a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea ma-
yor que el segundo.
c) Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?
"""

a=int(input("Ingrese un numero ==>"))

b=int(input("Ingrese un numero ==>"))

#a)
for i in range(a,b):
    if(i%a==0):
        if(i<b and i>a):
            print("El siguiente numero es multiplo de a y menor que b ==>",i)
#b)
print("Apartado b")
c=a
j=2
while((a*j)<b):
    print("El siguiente numero es multiplo de a y menor que b ==>",a*j)
    j=j+1