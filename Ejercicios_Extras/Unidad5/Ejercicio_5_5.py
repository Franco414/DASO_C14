"""
Ejercicio 5.5. Algoritmo de Euclides
a) Implementar en python el algoritmo de Euclides para calcular el máximo común divisor de dos
números n y m, dado por los siguientes pasos.
1. Teniendo n y m, se obtiene r, el resto de la división entera de m/n.
2. Si r es cero, n es el mcd de los valores iniciales.
3. Se reemplaza m ← n, n ← r, y se vuelve al primer paso.
b) Hacer un seguimiento del algoritmo implementado para los siguientes pares de números: (15,9);
(9,15); (10,8); (12,6).
"""

from mmap import MAP_EXECUTABLE


def obtener_mcd(m,n):
    mcd=0
    continuar=True
    while(continuar):
        r=m%n
        if r==0:
            mcd=n
            continuar=False
        else:
            m=n
            n=r
    return mcd

m_u =int(input("Ingrese el numero m"))
n_u =int(input("Ingrese el numero n"))
res=obtener_mcd(m_u,n_u)
print("El mcd de %d y %d es ==> %d"%(m_u,n_u,res))
