"""
a) Escribir una funcion llamada map, que reciba una función y una lista y devuelva la lista que
resulta de aplicar la función recibida a cada uno de los elementos de la lista recibida.
b) Escribir una función llamada filter, que reciba una función y una lista y devuelva una lista con
los elementos de la lista recibida para los cuales la función recibida devuelve un valor verdadero.
c) ¿En qué ejercicios de esta guía podría haber utilizado estas funciones?
"""
#a)
def map(funcion,lista):
    lista_res=[]
    for i in lista:
        lista_res.append(funcion(i))
    return lista_res
#funcion a probar
def area_cuadrado(numero):
    return numero*numero

p=[3,4,5,6]
l=map(area_cuadrado,p)
print(l)
#b)
def filter(funcion,lista):
    lista_res=[]
    for i in lista:
        if funcion(i):
            lista_res.append(i)
    return lista_res
#funcion a probar
def es_par(numero):
    return numero%2==0

d=[3,4,5,6,7,8,9,10]
l=filter(es_par,d)
print(l)