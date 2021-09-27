"""
Ejercicio 4.6. Suponiendo que el primer día del año fue lunes, escribir una función que reciba un número
con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo: si recibe ’3’ debe
devolver ’miércoles’, si recibe ’9’ debe devolver ’martes’
"""
def obtener_dia(numero):
    dias=["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
    indice=1
    aux=numero
    while(aux>8):
        aux=aux-7
    while(aux):
        aux=aux-1
        indice=indice+1
        indice=indice%7
    return dias[indice]

print(obtener_dia(144))