"""
Ejercicio 5.8. Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales
(primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de salida). Al final, el
programa debe imprimir cuántos números fueron ingresados, la suma total de los valores y el promedio.
"""

n=0
s=0
p=0
continuar=True
while(continuar):
    x=int(input("Ingrese un numero ==> "))
    if(x==-1):
        continuar=False
        p=s/n
    else:
        n=n+1
        s=s+x
print("Se ingresaron esta cantidad de numeros==>",n)
print("La suma de todos los numero enteros ingresados es de => ",s)
print("El promedio de los numeros ingresados es de ==> ",p)