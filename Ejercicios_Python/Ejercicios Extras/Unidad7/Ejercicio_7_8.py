"""
a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea igual
a la original pero invertida. Así, dada la lista [’Di’, ’buen’, ’día’, ’a’, ’papa’],
deberá devolver [’papa’, ’a’, ’día’, ’buen’, ’Di’].
b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modifique la lista
dada para invertirla, si usar listas auxiliares.
"""
#a)
def obt_lista_invertida(lista):
    lista_aux=[]
    for i in range(len(lista)-1,-1,-1):
        lista_aux.append(lista[i])
    return lista_aux

lista=["far",23,4.232,323,"hola"]
lista2=obt_lista_invertida(lista)
print(lista2)

#b)
def obt_lista_invertida_2(lista):
    lista.reverse()
    return

lista2=["hola",2,34,45.43,"chau"]
obt_lista_invertida_2(lista2)
print(lista2)