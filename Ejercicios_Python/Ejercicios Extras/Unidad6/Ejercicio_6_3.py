"""
Modificar las funciones anteriores, para que reciban un parámetro que indique la cantidad
máxima de reemplazos o inserciones a realizar.
"""
#a)
def my_function_string_a(caracter,cadena,maxRe):
    lista=[]
    countRemp=0
    for i in range(0,len(cadena)):
        lista.append(cadena[i])
        if (countRemp<maxRe):
            lista.append(caracter)
            countRemp=countRemp+1
    ret="".join(lista)
    return ret
        

cad=my_function_string_a("a","Hola mundo",3)
print(cad)
#b)
def my_function_string_b(caracter,cadena,maxRe):
    lista=[]
    countRemp=0
    for i in range(0,len(cadena)):
        if(cadena[i]!=" "):
                lista.append(cadena[i])
        else:
            if(countRemp<maxRe):
                lista.append(caracter)
                countRemp=countRemp+1
            else:
                lista.append(cadena[i])
    ret="".join(lista)
    return ret

cad=my_function_string_b("_","Prueba de cadena abc",2)
print(cad)
#c)
def my_function_string_c(caracter,cadena,maxRe):
    lista=[]
    countRemp=0
    for i in range(0,len(cadena)):
        if(cadena[i]>='0' and cadena[i]<='9'):
            if(countRemp<maxRe):
                lista.append(caracter)
                countRemp=countRemp+1
            else:
                lista.append(cadena[i])
        else:
            lista.append(cadena[i])
    ret="".join(lista)
    return ret

cad=my_function_string_c("X", "Su contraseña es 4543",3)
print(cad)
#d)
def my_function_string_d(caracter,cadena,maxRe):
    lista=[]
    count=0
    i=0
    countRemp=0
    while(i<len(cadena)):
        if(count==3):
            if(countRemp<maxRe):
                lista.append(caracter)
                count=0
                countRemp=countRemp+1
            else:
                lista.append(cadena[i])
                i=i+1
        else:
            lista.append(cadena[i])
            i=i+1
            count=count+1
    ret="".join(lista)
    return ret

cad=my_function_string_d("@","234567890123",2)
print(cad)