"""
Ejercicio 1.2. Implementar algoritmos que permitan:
a) Calcular el perímetro y área de un rectángulo dada su base y su altura.
b) Calcular el perímetro y área de un círculo dado su radio.
c) Calcular el volumen de una esfera dado su radio.
d) Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1,x2,y1,y2.
e) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
"""
#a)
def rect1(base,altura):
    lista = []
    lista.append(base*2+altura*2)
    lista.append(base*altura)
    return lista
#b)
def circ1(radio):
    from math import pi
    lista = []
    lista.append(2*pi*radio)
    lista.append(pi*radio*radio)
    return lista
#c)
def volumen_esfera(radio):
    from math import pi
    volumen = pi*4/3
    volumen = volumen * radio
    volumen = volumen * radio
    volumen = volumen * radio
    return volumen
#d)
def area_rect1(x1,x2,y1,y2):
    aux=x1-x2
    aux2=y1-y2
    area = abs(aux)*abs(aux2)
    return area
#e)
def hipotenusa_triangulo_rect(cat1,cat2):
    from math import sqrt
    aux=cat1*cat1
    aux2=cat2*cat2
    aux=aux+aux2
    hipotenusa=sqrt(aux)
    return hipotenusa

print("[perimetro,base]")
print(rect1(4,5))
print("[perimetro,base]")
print(circ1(3))
print("volumen esfera")
print(volumen_esfera(3))
print("area de un rectangulo")
print(area_rect1(2,6,7,3,))
print("hipotenusa")
print(hipotenusa_triangulo_rect(3,4))