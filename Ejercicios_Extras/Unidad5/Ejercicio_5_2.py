"""
Ejercicio 5.2. Escribir una función que reciba un número entero k e imprima su descomposición en
factores primos.
"""
factores=[]

numero=int(input("Ingrese un número ==>"))

es_negativo=False
numero_ingresado=numero

if numero<0:
    es_negativo=True
    numero_ingresado=numero_ingresado*(-1)
for i in range(2,numero_ingresado+1):
    es_primo=True
    for j in range(2,i):
        if i%j==0:
            es_primo=False
    if es_primo==True:
        if(es_negativo):
            factores.append(i*(-1))
        else:
            factores.append(i)

if numero==1 or numero==0 or numero==-1:
    print("el número %d no tiene factores primos"%numero)
else:
    print("Los factores primos del numero %d son"%numero)
    print(factores)