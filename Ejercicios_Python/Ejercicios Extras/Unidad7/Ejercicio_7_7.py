"""
Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Ini-
cial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el nombre,
luego la inicial con un punto, y luego el apellido.
"""
def my_string(lista):
    lista_2=[]
    for i in range(0,len(lista)):
        aux=lista[i][1]+" "+lista[i][2]+". "+lista[i][0]
        lista_2.append(aux)
    return lista_2

lista=[("martinez","Ines","L"),("Roten","Carlos","A"),("Roger","Steve","C"),("Magallan","Luciana","F")]
lista2=my_string(lista)
print(lista2)