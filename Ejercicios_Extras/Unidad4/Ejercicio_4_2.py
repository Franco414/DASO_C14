"""
Ejercicio 4.2. Escribir una implementación propia de la función abs, que devuelva el valor absoluto de
cualquier valor que reciba.
"""
def my_abs(numero):
    resultado=numero
    if numero<0:
        resultado=resultado*-1
    return resultado

x=float(input("Ingrese un número"))
y=my_abs(x)
print("El valor absoluto del número es, ",y)