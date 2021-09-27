"""
a) Escribir una función que reciba dos vectores y devuelva su producto escalar.
b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.
c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
d) Escribir una función que reciba un vector y devuelva su norma.
"""
def obt_producto_escalar(vector_a,vector_b):
    if(len(vector_a)!=len(vector_b)):
        ret=-1
    else:
        ret=0
        for i in range(0,len(vector_a)):
            ret=ret+vector_b[i]*vector_a[i]
    return ret

a=(3,2,5)
b=(1,6,4)
res=obt_producto_escalar(a,b)
print("el producto escalar es ==>",res) 
#b)
def son_ortogonales(vector_a,vector_b):
    res=obt_producto_escalar(vector_a,vector_b)
    if(res==0):
        ret=True
    else:
        ret=False
    return ret

a=(0,2,3)
b=(18,3,4)
res=son_ortogonales(a,b)
if(res):
    print("Los vectores son ortogonales")
else:
    print("Los vectores no son ortogonales")
#d)
def obt_norma_vector(vector):
    from math import sqrt
    norma=0
    aux=0
    for i in range(0,len(vector)):
        aux=aux+vector[i]*vector[i]
    norma=sqrt(aux)
    return norma
c=(4,2,5)
res=obt_norma_vector(c)
print("La norma del vector es ==>",res)
#c)
def son_paralelos(vector_a,vector_b):
    aux=obt_producto_escalar(vector_a,vector_b)
    norma_A=obt_norma_vector(vector_a)
    norma_B=obt_norma_vector(vector_b)
    aux2=norma_A*norma_B
    if(aux==aux2 or aux==(aux2*-1)):
        ret=True
    else:
        ret=False
    return ret

va=(2,4,6)
vb=(-1,-2,-3)
if(son_paralelos(va,vb)):
    print("Los vectores son paralelos")
else:
    print("Los vectores no son paralelos")