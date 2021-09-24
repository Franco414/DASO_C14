"""
Ejercicio 1.1. Escribir un programa que pregunte al usuario:
a) su nombre, y luego lo salude.
b) dos números y luego muestre el producto.
"""
nombre = input("Ingrese su nombre: ")
print("Hola "+nombre)
x=int(input("Ingrese un numero: "))
y=int(input("Ingrese otro numero: "))
z=x*y
print("El producto de los dos números es " +str(z))