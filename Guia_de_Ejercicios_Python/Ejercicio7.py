"""
7. Dado el archivo de configuración “config.txt” el cual tiene el formato clave=valor en cada una
de sus líneas, escribir una función que reciba el nombre del archivo y devuelva un diccionario con
los valores especificados en el archivo.
NOTA: Utilizar las funciones split() y strip()
"""

"""
Ejemplo config.txt

car=rojo
fruta=manzana
"""

def es_float(cadena):
    ret=False
    char_invalido =False
    salir =True
    empieza_numero=False
    parte_decimal=False
    if cadena[0]=='+' or cadena[0]=='-':
        salir=False
    else:
        if cadena[0]=='.':
            parte_decimal=True
            salir=False
        else:
            if cadena[0]>='0' and cadena[0]<='9':
                salir=False
                empieza_numero=True
            else:
                salir=True
    if salir ==False and len(cadena)>1:
        ret=True
        for i in (1,len(cadena)-1):
            if parte_decimal==True and cadena[i]=='.':
                char_invalido=True
                break
            else:
                if cadena[i] == '.':
                    parte_decimal=True
                else:
                    if cadena[i]<'0' or cadena[i]>'9':
                        char_invalido=True
                        break
    if char_invalido==True or cadena[len(cadena)-1]=='.':
        ret=False
    if parte_decimal==False:
        ret=False
    return ret

def get_dic(nombre):
    lista2 = []
    lista_clave=[]
    lista_valor=[]
    with open("/home/franco-unt/Documents/14CESE2021/DASO/Guia_de_Ejercicios_Python/"+nombre+".txt","r") as archivo:
        for cadena in archivo:
            #lista = cadena.split(sep='n')
            aux = cadena.strip()
            lista=aux.split('=')
            lista_clave.append(lista[0])
            if es_float(lista[1])==True:
                numero_float=float(lista[1])
                lista_valor.append(numero_float)
            else:
                if lista[1].isdigit() == True:
                    num = int(lista[1])
                    lista_valor.append(num)
                else:    
                    lista_valor.append(lista[1])
    print(lista_clave)
    print(lista_valor)
    d = dict(zip(lista_clave,lista_valor))
    print(d)

get_dic("config")