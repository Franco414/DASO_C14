"""
Ejercicio 1.5. Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces,
con espacios intermedios.
"""
palabra=input("Ingrese una palabra")

for i in range(0,100):
    print(palabra,end=" ")

print(" ",end ='\n')
print("chau")