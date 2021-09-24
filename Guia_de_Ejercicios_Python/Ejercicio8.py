"""
8. Escribir una función que reciba un diccionario y escriba en un archivo cuyo nombre se recibe
también como argumento, los datos en formato clave=valor.
"""

def dic2txt(diccionario,nombre):
    lista_claves = list(diccionario.keys())
    lista_valores = list(diccionario.values())
    print(lista_claves)
    print(lista_valores)
    
    with open("/home/franco-unt/Documents/14CESE2021/DASO/Guia_de_Ejercicios_Python/"+nombre,"a") as archivo:
        for i in range(0,len(lista_claves)):
            aux = '\n'+lista_claves[i]+'='+str(lista_valores[i])
            archivo.write(aux)
    
    

name="config.txt"
d = {'hola':'chau','edad':2,'pi':3.14,'apellido':'ingresar'}
dic2txt(d,name)