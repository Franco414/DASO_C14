"""
a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima el mensaje
Estimado <nombre>, vote por mí.
b) Escribir una función que reciba una tupla con nombres, una posición de origen py una cantidad
n, e imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición p.
c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario, para ello,
deberán recibir una tupla de tuplas, conteniendo el nombre y el género.
"""
#a)
def print_all_names(tupla):
    for i in tupla:
        print("Estimado %s, vote por mí"%i)

a=("franco","alejandra","andrea","paula","erica","lucia","mateo")
#print_all_names(a)
#b)
def print_names_a(tupla,p,n):
    for i in range(p,n+p):
        print("Estimado %s, vote por mí"%tupla[i])

#print_names_a(a,2,3)
#c)
def print_names_b(tupla,p,n):
    aux=p
    if(aux<0 or aux>=len(tupla)):
        aux=0
    aux2=p+n
    if(aux2<0 or aux2>=len(tupla)):
        aux2=len(tupla)
    for i in range(aux,aux2):
        if(tupla[i][1]=="m"):
            print("Estimado %s, vote por mí"%tupla[i][0])
        else:
            print("Estimada %s, vote por mí"%tupla[i][0])

b=(("franco","m"),("lucia","f"),("lucas","m"),("eric","m"),("andrea","f"),("ana","f"),("daniel","m"))

#print_names_b(b,2,4)

def print_names_c(tupla):
    for i in range(0,len(tupla)):
        if(tupla[i][1]=="m"):
            print("Estimado %s, vote por mí"%tupla[i][0])
        else:
            print("Estimada %s, vote por mí"%tupla[i][0])

print_names_c(b)