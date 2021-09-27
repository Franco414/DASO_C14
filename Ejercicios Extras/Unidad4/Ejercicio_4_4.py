"""
Ejercicio 4.4. Escribir funciones que permitan encontrar:
a) El máximo o mínimo de un polinomio de segundo grado (dados los coeficientes a, b y c),
indicando si es un máximo o un mínimo.
b) Las raíces (reales o complejas) de un polinomio de segundo grado.
Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por cero, ni
calcular la raíz de un número negativo).
c) La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta).
Nota: validar que no sean dos rectas con la misma pendiente, antes de efectuar la operación.
"""

#a)
def obt_max_min_parabola(a,b,c):
    vertice=-b/(2*a)
    resultado=a*vertice*vertice
    resultado=resultado+b*vertice
    resultado=resultado+c
    return resultado

a=3
b=2
c=0
maximo=obt_max_min_parabola(a,b,c)
print("El maximo de la parabola {0}x^2+{1}x+{2} es ==> {3}".format(a,b,c,maximo))
#b)
def raices_parabola(a,b,c):
    from math import sqrt
    x=[]
    aux=b*b-4*a*c
    aux2=0
    s1=[]
    s2=[]
    if aux>0:
        aux=sqrt(aux)
        aux2=-b+aux
        x.append(aux2/(2*a))
        aux2=-b-aux
        x.append(aux2/(2*a))
    else:
        if aux==0:
            aux2=-b/(2*a)
            x.append(aux2)
            x.append(aux2)
        else:
            aux3=aux*(-1)
            aux3=sqrt(aux3)
            aux4=0
            aux2=-b/(2*a)
            s1.append(aux2)
            aux4=aux3/(2*a)
            s1.append(aux4)
            aux2=-b/(2*a)
            s2.append(aux2)
            aux4=aux3*(-1)
            aux4=aux4/(2*a)
            s2.append(aux4)
            x.append(s1)
            x.append(s2)
    return x

raices=raices_parabola(1,2,3)
print("las raices del polinomio ",raices)