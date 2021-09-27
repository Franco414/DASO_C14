"""
Ejercicio 5.4. Utilizando la función randrange del módulo random, escribir un programa que obten-
ga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique sin son menores
o mayores que el número a adivinar, hasta que el usuario ingrese el número correcto.
"""

def adivinar_numero():
    from random import randrange
    numero=0
    print("Bienvenido!! Intenta adivinar el número")
    numero=randrange(0,100)
    adivino=False
    while(adivino==False):
        numero_usuario=int(input("Ingrese un nuevo número ==> "))
        if(numero_usuario==numero):
            adivino=True
            print("Felicidades adivino el numero")
        else:
            if(numero_usuario<numero):
                print("El numero ingresado es menor al numero que pieso")
            else:
                print("El numero ingresado es mayor al numero que pieso")

adivinar_numero()