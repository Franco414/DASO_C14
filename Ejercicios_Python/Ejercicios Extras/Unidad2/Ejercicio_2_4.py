"""
Ejercicio 2.4. Escribir un programa que imprima todos los números pares entre dos números que se le
pidan al usuario.
"""
a = int(input("ingrese un numero"))
b = int(input("ingrese otro numero"))
while(a==b):
    print("El número ingresado esta repetido")
    b = int(input("ingrese otro numero"))
if(a<b):
    inf=a
    sup=b
else:
    inf=b
    sup=a
for i in range(inf,sup):
    if(i%2==0):
        print(i)