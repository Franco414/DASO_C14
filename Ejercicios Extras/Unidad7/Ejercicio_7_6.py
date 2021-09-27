"""
Dada una lista de números enteros y un entero k, escribir una función que:
a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
b) Devuelva una lista con aquellos que son múltiplos de k.
"""
#a)
def my_user_a(lista,k):
    lista_a=[]
    lista_b=[]
    lista_c=[]
    for i in lista:
        if(i==k):
            lista_c.append(i)
        else:
            if(i<k):
                lista_a.append(i)
            else:
                lista_b.append(i)
    return lista_a,lista_b,lista_c

lista=[3,4,5,23,66,1,89,324,41,3,4,51,12]
l1,l2,l3=my_user_a(lista,50)
print(l1)
print(l2)
print(l3)
#b)
def my_user_b(lista,k):
    ret_lista=[]
    for i in lista:
        if(i%k==0):
            ret_lista.append(i)
    return ret_lista

lista=[2,3,4,6,8,10,13,26,35,25,14,18]
lista2=my_user_b(lista,4)
print(lista2)