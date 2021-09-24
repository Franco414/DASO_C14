def get_dic(nombre):
    lista2 = []
    lista_clave=[]
    lista_valor=[]
    with open("/home/franco-unt/Documents/14CESE2021/DASO/Guia_de_Ejercicios_Python/"+nombre,"r") as archivo:
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
    return d

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

def dic2txt(diccionario,nombre):
    lista_claves = list(diccionario.keys())
    lista_valores = list(diccionario.values())
    print(lista_claves)
    print(lista_valores)
    
    with open("/home/franco-unt/Documents/14CESE2021/DASO/Guia_de_Ejercicios_Python/"+nombre,"a") as archivo:
        for i in range(0,len(lista_claves)):
            aux = '\n'+lista_claves[i]+'='+str(lista_valores[i])
            archivo.write(aux)