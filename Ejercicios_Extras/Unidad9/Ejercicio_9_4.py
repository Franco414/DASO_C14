"""
Escribir una función que reciba un texto y para cada caracter presente en el texto devuelva
la cadena más larga en la que se encuentra ese caracter.
"""
def funcion(nombre):
    archivo=open(nombre,"r")
    contenido=archivo.read()
    lista=contenido.split(" ")
    indice=0
    d=dict()
    max=0
    for i in range(0,len(contenido)):
        ch=contenido[i]
        if(ch!=" "):
            max=0
            for j in range(0,len(lista)):
                count=0
                for k in lista[j]:
                    if(k==ch):
                        count=count+1
                if(max<count):
                    max=count
                    indice=j
            d[ch]=lista[indice]
    return d

ruta= "/home/franco-unt/Documents/14CESE2021/DASO/Ejercicios_Extras/Unidad9/archivo.txt"
d=funcion(ruta)
print(d)