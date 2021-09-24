#4. Escribir la función “es_par()” la cual recibe un número entero y devuelve True si el número es
#par o False si es impar.

def es_par(number):
    ret = False
    if number % 2 == 0:
        ret=True
    return ret

number =5

probar = es_par(number)

if probar:
    msg ="el número %d es par."%(number)
    print(msg)
else:
    msg ="el número %d es impar."%(number)
    print(msg)