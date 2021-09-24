"""
Ejercicio 2.2. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
Recordar que la fórmula para la conversión es: F = (9/5)*C + 32
"""
f = float(input("Ingrese una temperatura en grados Fahrenheit: "))

aux=f-32
c=aux*5/9
print("La temperatura ingresa en grados Celsius es:",c)