"""
Escribir una función que reciba una tupla de elementos e indique si se encuentran orde-
nados de menor a mayor o no.
"""
def det_tupla_estaOrdenada(tupla):
    ret=True
    for i in range(0,len(tupla)-1):
        if(tupla[i]>tupla[i+1]):
            ret=False
    return ret

a=(3,3,2,6,7)
if(det_tupla_estaOrdenada(a)):
    print("La tupla esta ordenada")
else:
    print("La tupla no esta ordenada")