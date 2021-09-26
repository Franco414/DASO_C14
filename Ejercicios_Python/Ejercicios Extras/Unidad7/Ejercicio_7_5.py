"""
Dada una lista de números enteros, escribir una función que:
a) Devuelva una lista con todos los que sean primos.
b) Devuelva la sumatoria y el promedio de los valores.
c) Devuelva una lista con el factorial de cada uno de esos números.
"""
def es_primo(numero):
    resultado=True
    if numero>=-1 and numero<=1:
        return resultado
    for i in range(2,numero):
        if numero%i==0:
            resultado=False
            break
    return resultado
#a)
def obt_lista_numeros_primos(lista):
    lista_n_primos=[]
    for i in lista:
        if(es_primo(i)):
            lista_n_primos.append(i)
    return lista_n_primos

lista=[3,4,1,5,6,7,8,9,13,10]
lista2=obt_lista_numeros_primos(lista)
print(lista2)
#b)
def my_user_b(lista):
    sum=0
    pro=0
    for i in lista:
        sum=sum+i
    pro=sum/len(lista)
    return sum,pro

lista=[1,2,3,4,5,6]
s,p=my_user_b(lista)
print("La sumatoria de los numeros de la lista es => %d y su promedio es %f"%(s,p))
#c)
def encontrar_factorial(numero):
    factorial = 1
    for i in range(1,numero+1):
        factorial=factorial*i
    return factorial

def my_user_c(lista):
    ret_lista=[]
    for i in lista:
        ret_lista.append(encontrar_factorial(i))    
    return ret_lista

lista3=my_user_c(lista)
print(lista3)