"""
Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
a) La primera letra de cada palabra. Por ejemplo, si recibe ’Universal Serial Bus’ debe
devolver ’USB’.
b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
’república argentina’ debe devolver ’República Argentina’.
c) Las palabras que comiencen con la letra ’A’. Por ejemplo, si recibe ’Antes de ayer’ debe
devolver ’Antes ayer’
"""
#a)
def my_string_a(cadena):
    lista=[]
    ban=1
    for i in range(0,len(cadena)):
        if(cadena[i]==" "):
            ban=1
        else:
            if(ban==1):
                lista.append(cadena[i])
                ban=0
    ret="".join(lista)
    return ret

cad=my_string_a("Universal Serial Bus")
print(cad)
#b)
def my_string_b(cadena):
    lista=[]
    ban=1
    for i in range(0,len(cadena)):
        if(cadena[i]==" "):
            ban=1
        else:
            if(ban==1):
                if(cadena[i]>="a" and cadena[i]<="z"):
                    lista.append(cadena[i].upper())
                else:
                    lista.append(cadena[i])
                ban=0
    ret="".join(lista)
    return ret

cad=my_string_b("universal serial bus")
print(cad)
#c)
def my_string_c(cadena):
    lista=[]
    ban=1
    guardar=0
    for i in range(0,len(cadena)):
        if(cadena[i]==" "):
            ban=1
            guardar=0
        else:
            if(ban==1):
                if(cadena[i]=="a"):
                    guardar=1
            ban=0
        if(guardar==1 or cadena[i]==" "):
            lista.append(cadena[i])
    ret="".join(lista)
    return ret

cad=my_string_c("aniversal serial aus")
print(cad)