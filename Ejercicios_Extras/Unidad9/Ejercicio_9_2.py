"""
a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apa-
riciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy"debe
devolver: ’que’: 2, ’lindo’: 1, ’día’: 1, ’hace’: 1, ’hoy’: 1
b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena de
texto, y los devuelva en un diccionario.
c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y
devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados.
Nota: utilizar el módulo random para obtener tiradas aleatorias.
"""
from typing import Counter


def funcion_a(cadena):
    d=dict()
    l=cadena.split(" ")
    claves_procesada=[]
    for i in range(0,len(l)):
        analizar=True
        clave=l[i]
        for c in claves_procesada:
            if(c.lower()==clave.lower()):
                analizar=False
        if(analizar):
            claves_procesada.append(clave)
            count=0
            for j in range(0,len(l)):
                if clave.lower()==l[j].lower():
                    count=count+1
            d[clave]=count
    return d

#e=funcion_a("Que lindo día que hace hoy")
#print(e)
#b)
def funcion_b(cadena):
    d=dict()
    chars_read=[]
    for i in range(0,len(cadena)):
        analizar=True
        ch=cadena[i]
        for c in chars_read:
            if(c.lower()==ch.lower()):
                analizar=False
        if(analizar):
            chars_read.append(ch)
            count=0
            for j in range(0,len(cadena)):
                if ch.lower()==cadena[j].lower():
                    count=count+1
            d[ch]=count
    return d

e=funcion_b("Que lindo día que hace hoy")
print(e)
#c)
def observar_dados(n):
    d=dict()
    lista=[]
    from random import randint
    for i in range(0,n):
        x=randint(1,6)
        y=randint(1,6)
        lista.append((x,y))
    for i in range(0,len(lista)):
        s=lista[i][0]+lista[i][1]
        count=0
        for j in range(0,len(lista)):
            aux=lista[j][0]+lista[j][1]
            if(aux==s):
                count=count+1;
        d[str(s)]=count
    return d
print("Apartado c")
f=observar_dados(100)
print(f)