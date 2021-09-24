"""
Escribir funciones que dada una cadena de caracteres:
a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe ’algoritmos’ o
’logaritmos’ debe devolver ’lgrtms’.
b) Devuelva solamente las letras vocales. Por ejemplo, si recibe ’sin consonantes’ debe
devolver ’i ooae’.
c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe ’vestuario’ debe de-
volver ’vistaerou’.
d) Indique si se trata de un palíndromo. Por ejemplo, ’anita lava la tina’ es un palíndro-
mo (se lee igual de izquierda a derecha que de derecha a izquierda).
"""
#a)
from abc import abstractproperty


def get_letter_not_vowels(cadena):
    lista = []
    vocal =["a","e","i","o","u","A","E","I","O","U"]
    es_vocal=False
    for i in range(0,len(cadena)):
        for j in vocal:
            if(cadena[i]==j):
                es_vocal=True
        if (es_vocal==False):
            lista.append(cadena[i])
        es_vocal=False
    ret="".join(lista)
    return ret

cad=get_letter_not_vowels("Este Es UnA prueba de hoy")
print(cad)
#b)
def get_letters_vowels(cadena):
    lista=[]
    vocal =["a","e","i","o","u","A","E","I","O","U"]
    es_vocal=False
    for i in range(0,len(cadena)):
        for j in vocal:
            if(cadena[i]==j):
                es_vocal=True
        if(es_vocal or cadena[i]==" "):
            lista.append(cadena[i])
        es_vocal=False
    ret="".join(lista)
    return ret

cad=get_letters_vowels("sin consonantes")
print(cad)
#c)
def my_string_vowels(cadena):
    lista=[]
    es_vocal=False
    indice=0
    vocal =[["a","e"],["e","i"],["i","o"],["o","u"],["u","a"],["A","E"],["E","I"],["I","O"],["O","U"],["U","A"]]
    for i in range(0,len(cadena)):
        for j in range(0,len(vocal)):
            if(cadena[i]==vocal[j][0]):
                es_vocal=True
                indice=j
        if(es_vocal):
            lista.append(vocal[indice][1])
        else:
            lista.append(cadena[i])
        es_vocal=False
    ret="".join(lista)
    return ret

cad=my_string_vowels("sin consonantes")
print(cad)
#d)
def det_palindromo(cadena):
    lista=[]
    i=0
    es_palindromo=True
    j=len(cadena)-1
    while(i<(len(cadena)-1) and j>=0):
        while(cadena[j]==" "):
            j=j-1
        while(cadena[i]==" "):
            i=i+1
        if(cadena[i]!=cadena[j]):
            es_palindromo=False
        i=i+1
        j=j-1
    if(es_palindromo):
        print("la cadena es un palindromo")
    else:
        print("la cadena no es un palindromo")

det_palindromo("anita lava la tina")