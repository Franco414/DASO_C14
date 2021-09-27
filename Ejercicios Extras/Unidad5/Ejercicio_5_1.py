"""
Ejercicio 5.1. Escribir un programa que reciba una a una las notas del usuario, preguntando a cada paso
si desea ingresar más notas, e imprimiendo el promedio correspondiente.
"""

repetir = True
promedio=0
auxiliar=0
indice=0
while(repetir):
    nota=input("Ingrese una nueva nota o la letra N para finalizar")
    if nota=='N':
        repetir=False
    else:
        if nota.isdigit()==True:
            indice=indice+1
            promedio=promedio+int(nota)
            auxiliar=promedio/indice
            print("El promedio hasta el momento es de ==>",auxiliar)
if indice>0:
    promedio=promedio/indice
print("El promedio de todas las notas es ==>",promedio)