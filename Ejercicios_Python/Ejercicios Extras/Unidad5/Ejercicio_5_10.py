"""
Ejercicio 5.10. Escribir una función que reciba un número natural e imprima todos los números primos
que hay hasta ese número.
"""
def es_primo(numero):
    resultado=True
    if numero>=-1 and numero<=1:
        return resultado
    for i in range(2,numero):
        if numero%i==0:
            resultado=False
            break
    return resultado

def get_all_numbers_counsins():
    n=int(input("Ingrese un numero ==>"))
    for i in range(2,n):
        if(es_primo(i)):
            print("el siguiente numero, es primo ==> ",i)

get_all_numbers_counsins()