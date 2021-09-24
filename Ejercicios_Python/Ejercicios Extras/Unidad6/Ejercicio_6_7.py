"""
Escribir funciones que dadas dos cadenas de caracteres:
a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, ’cadena’ es una
subcadena de ’subcadena’.
b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe ’kde’ y ’gnome’
debe devolver ’gnome’.
"""
#a) 
def find_subArray_into_string(cadena,subCadena):
    return subCadena in cadena

if(find_subArray_into_string("hoy es un dia maravilloso","dia")):
    print("la subcadena esta en la cadena")
else:
    print("la subcadena no esta en la cadena")

#b)
def return_first_string_in_alphabetic_order(cadena_a,cadena_b):
    lista=[]
    lista.append(cadena_a[0])
    lista.append(cadena_b[0])
    lista.sort()
    if(cadena_a[0]==lista[0]):
        ret=cadena_a
    else:
        ret=cadena_b
    return ret

cad=return_first_string_in_alphabetic_order("run","radio")
print(cad)