"""
Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo, telefono),
y busque dentro de la lista, todas las entradas que contengan en el nombre completo la cadena recibida
(puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos). Debe devolver una lista con
todas las tuplas encontradas.
"""
def get_info(buscar,lista):
    coincidencias=[]
    for i in range(0, len(lista)):
        if(buscar in lista[i][0]):
            coincidencias.append(lista[i])
    return coincidencias

d1=("elias antonio enrique","3875849124")
d2=("Eric david franco","3875849124")
d3=("melisa antonela erica","3875849124")
d4=("ana natalia lucia","3875849124")
d5=("gabriel rodriguez antonio","3875849124")
d6=("lucas rios ezequiel","3875849124")
d7=("rocio guantay","3875849124")
d8=("luciano colque","3875849124")
d9=("javier rivas","3875849124")
d10=("franco roberto","3875849124")
d11=("rosa david","3875849124")
d12=("matias ezequiel","3875849124")

guia=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]
matches=get_info("lucia",guia)
print(matches)