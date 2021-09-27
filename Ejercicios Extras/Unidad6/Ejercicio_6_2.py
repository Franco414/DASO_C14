"""
Escribir funciones que dada una cadena y un caracter:
a) Inserte el caracter entre cada letra de la cadena. Ej: ’separar’ y ’,’ debería devolver
’s,e,p,a,r,a,r’
b) Reemplace todos los espacios por el caracter. Ej: ’mi archivo de texto.txt’ y ’_’
debería devolver ’mi_archivo_de_texto.txt’
c) Reemplace todos los dígitos en la cadena por el caracter. Ej: ’su clave es: 1540’ y ’X’
debería devolver ’su clave es: XXXX’
d) Inserte el caracter cada 3 dígitos en la cadena. Ej. ’2552552550’ y ’.’ debería devolver
’255.255.255.0’
"""
#a)
def my_function_string_a(caracter,cadena):
    lista=[]
    for i in range(0,len(cadena)):
        lista.append(cadena[i])
        lista.append(caracter)
    ret="".join(lista)
    return ret
        

cad=my_function_string_a("a","Hola mundo")
print(cad)
#b)
def my_function_string_b(caracter,cadena):
    lista=[]
    for i in range(0,len(cadena)):
        if(cadena[i]!=" "):
            lista.append(cadena[i])
        else:
            lista.append(caracter)
    ret="".join(lista)
    return ret

cad=my_function_string_b("_","Prueba de cadena abc")
print(cad)
#c)
def my_function_string_c(caracter,cadena):
    lista=[]
    for i in range(0,len(cadena)):
        if(cadena[i]>='0' and cadena[i]<='9'):
            lista.append(caracter)
        else:
            lista.append(cadena[i])
    ret="".join(lista)
    return ret

cad=my_function_string_c("X", "Su contraseña es 4543")
print(cad)
#d)
def my_function_string_d(caracter,cadena):
    lista=[]
    count=0
    i=0
    while(i<len(cadena)):
        if(count==3):
            lista.append(caracter)
            count=0
        else:
            lista.append(cadena[i])
            i=i+1
            count=count+1
    ret="".join(lista)
    return ret

cad=my_function_string_d("@","234567890123")
print(cad)