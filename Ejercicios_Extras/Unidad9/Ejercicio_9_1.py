"""
Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde
las claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.
Por ejemplo:
l = [ (’Hola’, ’don Pepito’), (’Hola’, ’don Jose’), (’Buenos’, ’días’) ]
print tuplas_a_diccionario(l)
Deberá mostrar: { ’Hola’: [’don Pepito’, ’don Jose’], ’Buenos’: [’días’] }
"""
def funcion(lista):
    values=[]
    d=dict()
    for i in range(0,len(lista)):
        clave=lista[i][0]
        values=[]
        for j in range(0,len(lista)):
            if(clave==lista[j][0]):
                values.append(lista[j][1])
        d[clave]=values
    return d

l = [ ("Hola", "don Pepito"), ("Hola", "don Jose"), ("Buenos", "días") ]
e=funcion(l)
print(e)