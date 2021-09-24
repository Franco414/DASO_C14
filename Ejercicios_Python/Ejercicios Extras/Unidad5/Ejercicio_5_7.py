"""
Ejercicio 5.7. Números perfectos y números amigos
a) Escribir una función que devuelva la suma de todos los divisores de un número n, sin incluirlo.
b) Usando la función anterior, escribir una función que imprima los primeros m números tales que
la suma de sus divisores sea igual a sí mismo (es decir los primeros m números perfectos).
c) Usando la primera función, escribir una función que imprima las primeras m parejas de números
(a,b), tales que la suma de los divisores de a es igual a b y la suma de los divisores de b es igual a
a (es decir las primeras m parejas de números amigos).
d) Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de ejecución.
"""
#d)
#a)
def suma_divisores(numero):
    suma=0
    for i in range(1,numero):
        if numero%i==0:
            suma=suma+i
    return suma
"""
x=int(input("Ingresar un número"))

res=suma_divisores(x)
print("La suma de todos los divisores del numero %d es ==> %d"%(x,res))
"""
#b)
def n_numeros_perfectos(numero):
    lista=[]
    for i in range(2,numero):
        aux=suma_divisores(i)
        if(aux==i):
            lista.append(aux)
    print(lista)
    return
"""
x=int(input("Ingresar un número"))
n_numeros_perfectos(x)
"""
#c)
def pares_numAmigos(numero):
    count=0
    a_1=2
    b_1=0
    while(count<numero):
        aux=suma_divisores(a_1)
        aux2=suma_divisores(aux)
        if(a_1==aux2):
            print("(%d,%d)"%(a_1,aux))
            count=count+1
        a_1=a_1+1

x=int(input("Ingresar un número"))
pares_numAmigos(x)