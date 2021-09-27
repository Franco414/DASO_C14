"""
Escribir una función que reciba una lista desordenada y un elemento, que:
a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la cantidad de
coincidencias encontradas.
b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
c) Utilizando la función anterior, busque todos los elementos coincidan con el pasado por parámetro
y devuelva una lista con las posiciones.
"""
#a)
def get_match_element(lista,d):
    return lista.count(d)

lista=["hola",2,3.45,-2,"chau",3,14,2,"fra",2]
m=get_match_element(lista,2)
print("El elemento esta en la lista ==> %d veces"%m)
#b)
def get_index_match(lista,d):
    return lista.index(d)
print("Apartado b")
m=get_index_match(lista,2)
print("El elemento esta en la posicion ==> %d en la lista"%(m+1))
#c)
def get_index_match_2(lista,d):
    lista_res=[]
    for i in range(0,len(lista)):
        if(lista[i]==d):
            lista_res.append(i)
    return lista_res

print("Apartado c")
m=get_index_match_2(lista,2)
print(m)