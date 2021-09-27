"""
Escribir una función que reciba una lista ordenada y un elemento, si el elemento se en-
cuentra en la lista, debe encontrar su posición, mediante búsqueda binaria y devolverlo. Si no se en-
cuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición. (No utilizar
lista.sort())
"""
def busqueda_binaria(lista,elemento):
    inicio=0
    fin=len(lista)-1
    continuar=True
    while(continuar):
        indice=inicio+(fin-inicio)//2
        if(indice==0 or inicio==len(lista)):
            continuar=False
            indice=-1
        else:
            if inicio>fin:
                continuar=False
                indice=-1
            else:
                if(elemento==lista[indice]):
                    continuar=False
                else:
                    if(elemento<lista[indice]):
                        fin=indice-1
                    else:
                        inicio=indice+1
    return indice

"""
l=[3,4,5,6,7,8,9,10]
n=0
i=busqueda_binaria(l,n)
print("el elmento n==> %d se encuentra en la posicion ==> %d"%(n,i))
"""
def funcion(lista,elemento):
    mayor=0
    i=busqueda_binaria(lista,elemento)
    ret=len(lista)
    if i!=-1:
        ret=i
    else:
        i=0
        if(elemento<lista[0]):
            ret=0
        else:
            while(i<len(lista)):
                if elemento<lista[i]:
                    ret=i
                    i=len(lista)
                i=i+1
        lista.insert(ret,elemento)    
    return ret

l2=[3,4,5,7,8,9,10]
n=6
j=funcion(l2,n)
print("el elmento n==> %d se encuentra en la posicion ==> %d"%(n,j))
print(l2)