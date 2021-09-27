"""
Escribir funciones que dada una cadena de caracteres:
a) Imprima los dos primeros caracteres.
b) Imprima los tres últimos caracteres.
c) Imprima dicha cadena cada dos caracteres. Ej.: ’recta’ debería imprimir ’rca’
d) Dicha cadena en sentido inverso. Ej.: ’hola mundo!’ debe imprimir ’!odnum aloh’
e) Imprima la cadena en un sentido y en sentido inverso. Ej: ’reflejo’ imprime
’reflejoojelfer’.
"""

#a)
def print_two_first_characters(cadena):
    if(len(cadena)>=2):
        print(cadena[0])
        print(cadena[1])

print_two_first_characters("abc")

#b)
def print_three_last_characters(cadena):
    if(len(cadena)>=3):
        print(cadena[len(cadena)-3])
        print(cadena[len(cadena)-2])
        print(cadena[len(cadena)-1])

print_three_last_characters("franco")
#c)
def print_eachTwo_string(cadena):
    i=0
    while(i<len(cadena)):
        print(cadena[i],end="")
        i=i+2
    print("",end="\n")

print_eachTwo_string("recta hola mundo")
#d)
def print_reverse_string(cadena):
    for i in range(len(cadena)-1,0,-1):
        print(cadena[i],end="")
    print(cadena[0],"\n")

print_reverse_string("Prueba Cadena")