"""
Ejercicio 3.3. Área de un triángulo en base a sus puntos
a) Escribir una función que dado un vector al origen (definido por sus puntos x,y), devuelva la
�
norma del vector, dada por || (x, � y)|| = x 2 + y 2
b) Escribir una función que dados dos puntos en el plano (x1,y1 y x2,y2), devuelva la resta de
ambos (debe devolver un par de valores).
c) Utilizando las funciones anteriores, escribir una función que dados dos puntos en el plano
(x1,y1 y x2,y2), devuelva la distancia entre ambos.
d) Escribir una función que reciba un vector al origen (definido por sus puntos x,y) y devuelva un
vector equivalente, normalizado (debe devolver un par de valores).
e) Utilizando las funciones anteriores (b y d), escribir una función que dados dos puntos en el plano
(x1,y1 y x2,y2), devuelva el vector dirección unitario correspondiente a la recta que los une.
f) Escribir una función que reciba un punto (x,y), una dirección unitaria de una recta (dx,dy) y
un punto perteneciente a esa recta (cx,cy) y devuelva la proyección del punto sobre la recta.
Diseño del algoritmo:
1. Al punto a proyectar (x,y) restarle el punto de la recta (cx,cy)
2. Obtener la matriz de proyección P , dada por:
p 11 = d 2 x , p 12 = p 21 = d x ∗ d y , p 22 = d 2 y .
3. Multiplicar la matriz P por el punto obtenido en el paso 1:
r x = p 11 ∗ x + p 1 2 ∗ y, r y = p 21 ∗ x + p 22 ∗ y.
4. Al resultado obtenido sumar el punto restado en el paso 1, y devolverlo.
g) Escribir una función que calcule el área de un triángulo a partir de su base y su altura.
h) Utilizando las funciones anteriores escribir una función que reciba tres puntos en el plano
(x1,y1, x2,y2 y x3,y3) y devuelva el área del triángulo correspondiente.
"""
#a)
def norma_vector(x,y):
    from math import sqrt
    norma=x*x+y*y
    norma=sqrt(norma)
    return norma

print("la normal del vector (4,3) es, ",norma_vector(4,3))
#b)
def restar_2puntos(p1,p2):
    deltaY=p2[1]-p1[1]
    deltaX=p2[0]-p1[0]
    return deltaX,deltaY

a=[2,3]
b=[3,1]
c=restar_2puntos(a,b)
print("el vector diferencia es, ",c)
#c) 
def obtener_distancia(p1,p2):
    vector_distancia=restar_2puntos(p1,p2)
    distancia=norma_vector(vector_distancia[0],vector_distancia[1])
    return distancia

a=[4,5]
b=[3,3]
d=obtener_distancia(a,b)
print("la distancia entre los vectores es de, ",d)
#d)
def obt_vect_equivalente(x,y):
    norma= norma_vector(x,y)
    xn=x/norma
    yn=y/norma
    return xn,yn

print("ingrese un vector al origen dado por las cordenadas (x,y)")
x_vector=int(input("Ingrese la coordenada x del vector"))
y_vector=int(input("Ingrese la coordenada y del vector"))
vector_equivalente=obt_vect_equivalente(x_vector,y_vector)
print(vector_equivalente)
#e)
def obtener_vectUnit_entre2puntos(p1,p2):
    vector_distancia=restar_2puntos(p1,p2)
    vector_unitario=obt_vect_equivalente(vector_distancia[0],vector_distancia[1])
    return vector_unitario

print("el vector unitario con direccion igual a la distancia entre los puntos (4,5) y (1,6) es")
vector_unitario=obtener_vectUnit_entre2puntos([4,5],[1,6])
print(vector_unitario)
#f)
def obt_proy(punto,v_unitario,punto_recta):
    diferencia=restar_2puntos(punto_recta,punto)
    p11=v_unitario[0]*v_unitario[0]
    p12=v_unitario[0]*v_unitario[1]
    p21=p12
    p22=v_unitario[1]*v_unitario[1]
    rx=p11*diferencia[0]+p12*diferencia[1]
    ry=p21*diferencia[0]+p22*diferencia[1]
    ret_x=rx+punto_recta[0]
    ret_y=ry+punto_recta[1]
    return ret_x,ret_y

proyeccion=obt_proy([2,7],[0.6,0.8],[8,6])
print("La proyeccion del punto en la recta es",proyeccion)
#g)
def area_triangulo(base,altura):
    area=base*altura/2
    return area
res_area_triangulo=area_triangulo(8,3)
print("El area de un triangulo de base 8 y altura 3 es, ",res_area_triangulo)
#h)
#con dos puntos hallar el vector unitario
def obt_area_triangulo_3puntos(p1,p2,p3):
    (Xvu,Yvu)=obtener_vectUnit_entre2puntos(p1,p2)
    proyeccion_recta=obt_proy(p3,[Xvu,Yvu],p2)
    altura_vector=restar_2puntos(proyeccion_recta,p3)
    altura=norma_vector(altura_vector[0],altura_vector[1])
    base=obtener_distancia(p1,p2)
    ret_area=area_triangulo(base,altura)
    return ret_area

res_area_triangulo=obt_area_triangulo_3puntos([1,0],[3,0],[2,3])
print("area del triangulo1",res_area_triangulo)
res_area_triangulo=obt_area_triangulo_3puntos([1,2],[4,5],[4,0])
print("area del triangulo2",res_area_triangulo)