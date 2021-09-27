"""
Escribir una función que reciba un texto y una longitud y devuelva
una lista de cadenas de como máximo esa longitud. Las líneas deben ser cortadas correctamente en los
espacios (sin cortar las palabras).
"""

def separar_texto(nombre,longitud):
    lista=[]
    my_txt=open(nombre,"r")
    content=my_txt.read()
    inicio=0
    count=inicio
    fin=longitud
    continuar=True
    ban=True
    guardar=False
    if(len(content)<longitud):
        lista.append(content)
        continuar=False
    else:
        while(continuar):
            if(content[fin]!=" "):
                ban=True
                while(ban):
                    fin=fin-1
                    print(content[fin])
                    if(content[fin]==" "):
                        ban=False
                        guardar=True
                    if(fin<inicio):
                        ban=False
            else:
                guardar=True
            if guardar:
                lista.append(content[inicio:fin])
            guardar=False
            inicio=fin
            fin=inicio+longitud
            if(fin>len(content)):
                lista.append(content[inicio:len(content)-1])
                continuar=False
    return lista
dir_file="/home/franco-unt/Documents/14CESE2021/DASO/Ejercicios_Python/Ejercicios Extras/Unidad7/abrir.txt"
a=separar_texto(dir_file,50)
print(a)