"""
Escribir una función que reciba una lista de números no ordenada, que:
a) Devuelva el valor máximo.
b) Devuelva una tupla que incluya el valor máximo y su posición.
c) ¿Qué sucede si los elementos son cadenas de caracteres?
Nota: no utilizar lista.sort()
"""
#a)
def my_lista_a(lista):
    max=lista[0]
    for i in lista:
        if(max<i):
            max=i
    return max

l=[4,2,1,6,3,8,1,9,3,10,2,3,24,2,13,3]
m=my_lista_a(l)
print("El maximo de la lista es ==> ",m)
#b)
def my_lista_b(lista):
    max=lista[0]
    indice=0
    for i in range(0,len(lista)):
        if(max<lista[i]):
            max=lista[i]
            indice=i
    return (max,indice)

print("Apartado b")
tupla=my_lista_b(l)
print(tupla)

"""
l2=["hola",2,3,4,1,"adios",5,16,2,7,"franco","chau"]
print("Apartado c")
tupla2=my_lista_b(l2)
print(tupla2)
"""